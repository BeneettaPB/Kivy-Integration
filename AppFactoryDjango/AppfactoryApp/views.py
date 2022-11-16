import os
import sys
import json
import traceback
import multiprocessing
import pymysql

from django.db import connection, connections
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .import time
from .import base


category_mapper = {1: 'android', 2: 'ios', 3: 'common'}

BUILD_STATUS_UPDATE_ENDPOINT = f"https://{os.environ.get('host_addr')}/" \
                               f"ultimate-appfactory/build_status/update/by_build_id"

class BuildStatusManager:
    class DATA:
        class Platform:
            ANDROID = 1
            IOS = 2

            mapper = {
                ANDROID: 'android',
                IOS: 'ios'
            }

        class BuildStatus:
            FAILED = -1
            STANDBY = 0
            QUEUED = 1
            ONGOING = 2
            COMPLETED = 3

            mapper = {
                FAILED: 'FAILED',
                STANDBY: 'STANDBY',
                QUEUED: 'QUEUED',
                ONGOING: 'ONGOING',
                COMPLETED: 'COMPLETED'
            }
            verbose_message = {
                FAILED: "build failed!",
                STANDBY: "app initialised",
                QUEUED: "waiting in que for build to start",
                ONGOING: "build in progress...",
                COMPLETED: "build completed successfully",
                None: "requested item not found"
            }

            @classmethod
            def get_response_json_basic(cls, status_id_int, build_id=None, app_id=None, platform_id=None):
                out = {
                    'status': status_id_int in [cls.ONGOING, cls.COMPLETED],
                    'message': cls.verbose_message.get(status_id_int),
                    'data': {
                        'status': cls.mapper.get(status_id_int),
                        'status_code': status_id_int
                    }
                }
                if not out['message']:
                    if not platform_id:
                        out['message'] = 'unrecognised platform requested'

                if build_id:
                    out['data']['build_request_id'] = int(build_id)
                if app_id:
                    out['data']['build_app_id'] = int(app_id)
                if platform_id:
                    out['data']['build_platform'] = BuildStatusManager.DATA.Platform.mapper[platform_id]

                return out
    @staticmethod           
    def create_build_status(req_build_platform, app_id, version_name, user_id):
        build_status = BuildStatusManager.DATA.BuildStatus.ONGOING
        cursor = connection.cursor()

        cursor.execute(
            'SELECT app_version '
            'FROM app_factory_build_request '
            'WHERE app_id=%s AND platform=%s '
            'ORDER BY app_version DESC '
            'LIMIT 1',
            [app_id, req_build_platform]
        )
        db_read = cursor.fetchone()
        version_num = 1     # default value
        if db_read:
            if len(db_read):
                if db_read[0]:
                    version_num = int(db_read[0]) + 1
        timestamp_str = time.get_string_timestamp()
        cursor.execute(
            'INSERT INTO app_factory_build_request '
            '(app_id, platform, build_status, version_name, app_version, user_id, on_create, on_update) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            [
                app_id, req_build_platform, build_status, version_name, version_num, user_id,
                timestamp_str, timestamp_str
            ]
        )
        return str(cursor.lastrowid)

    @classmethod
    def view_status_by_app(cls, request, req_build_platform, app_id):
        cursor = connection.cursor()
        read_build_status, read_build_req_id = None, None

        platform_id = \
            [
                platform_id
                for platform_id, platform_name in cls.DATA.Platform.mapper.items()
                if platform_name == req_build_platform
            ] or None

        if platform_id:
            platform_id = platform_id[0]
            cursor.execute(
                'SELECT build_status, build_request_id '
                'from app_factory_build_request '
                'WHERE app_id=%s and platform=%s '
                'ORDER BY build_request_id DESC '
                'LIMIT 1',
                [app_id, platform_id]
            )
            row = cursor.fetchone()
            if row:
                read_build_status, read_build_req_id = row

        json_response = BuildStatusManager.DATA.BuildStatus.get_response_json_basic(
            status_id_int=read_build_status,
            build_id=read_build_req_id,
            app_id=app_id,
            platform_id=platform_id
        )
        return JsonResponse(json_response)

    @classmethod
    def view_status_by_build_id(cls, request, build_id):
        cursor = connection.cursor()
        cursor.execute(
            'SELECT build_status, app_id, platform '
            'FROM app_factory_build_request '
            'WHERE build_request_id=%s',
            [build_id]
        )
        row = cursor.fetchone()
        read_build_status_id, app_id, platform_id = row if row else (None, None, None)

        json_response = cls.DATA.BuildStatus.get_response_json_basic(
            status_id_int=read_build_status_id,
            build_id=build_id,
            platform_id=platform_id,
            app_id=app_id
        )
        return JsonResponse(json_response)

    @classmethod
    @csrf_exempt
    def update_status_by_build_id(cls, request, build_request_id=None, update_status=None):
        # necessary local variables
        history_table_map = {
            platform_options.ANDROID: 'app_factory_android_history',
            platform_options.IOS: 'app_factory_ios_history_advanced'
        }
        cursor = connection.cursor()

        # validate incoming request
        if request:
            build_request_id = request.POST.get('session_id')
            update_status = request.POST.get('app_status')
            if not (build_request_id and update_status):
                if int(update_status) not in build_status_options.mapper:
                    return JsonResponse({
                        'status': False,
                        'message': "bad request, SESSION_ID and STATUS required in post data"
                    })
        # change 1 to -1 until this value is updated in pods
        if int(update_status) == 1:
            update_status = -1

        print(f'starting update of build request {build_request_id} '
              f'to {build_status_options.mapper.get(int(update_status))}')

        # read meta data
        cursor.execute(
            'SELECT app_id, platform, build_status, version_name, app_version, user_id '
            'FROM app_factory_build_request '
            'WHERE build_request_id=%s',
            [build_request_id]
        )
        row = cursor.fetchone()
        app_id, platform_id, build_status, version_name, version_num, user_id \
            = row if row else (None, None, None, None, None)

        # update main table
        if int(update_status) == build_status_options.COMPLETED:
            no_ext_url = 'https://unitear.s3.ap-south-1.amazonaws.com/UltimateAppFactory' \
                      f'/app-{str(app_id)}/build-{str(build_request_id)}/app'
        else:
            no_ext_url = None
        timestamp_str = time.get_string_timestamp()
        cursor.execute(
            'UPDATE app_factory_build_request '
            'SET build_status=%s, app_apk_url=%s, app_bundle_url=%s, app_version=%s, on_update=%s '
            'WHERE build_request_id=%s',
            [
                update_status,
                no_ext_url+".apk" if no_ext_url else '',
                no_ext_url+".aab" if no_ext_url else '',
                int(version_num)+1 if update_status == build_status_options.ONGOING else version_num,
                timestamp_str,
                build_request_id
            ]
        )

        history_table = None
        # if update status is COMPLETE: then add entry to android & ios history table.
        if int(update_status) == build_status_options.COMPLETED:
            # check read values looked up from build id are valid before proceeding
            if app_id and version_name:
                history_table = history_table_map[int(platform_id) if platform_id else None]
                cursor.execute(
                    f'INSERT INTO {history_table} '
                    '(user_id, app_id, queue_id, version_name, app_version, apk_url, aab_url, oncreate, onupdate) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    [user_id, app_id, build_request_id, version_name, version_num,
                     f"{no_ext_url}.apk", f"{no_ext_url}.aab", timestamp_str, timestamp_str]
                )
            else:
                print('internal error: looked-up data from db of build_request invalid')
                return JsonResponse({
                    'status': False,
                    'message': 'internal error: looked-up data from db of build_request invalid'
                })

        print('-'*20 + f'ENDPOINT: build status update >>>\n'
              f'build_id: {str(build_request_id)}\n'
              f'app_id: {str(app_id)}\n'
              f'ver_nm: {str(version_name)}\n'
              f'ver_no: {str(version_num)}\n'
              f'platform: {platform_options.mapper.get(platform_id)}\n'
              f'to status: {build_status_options.mapper.get(int(update_status))}\n'
              f'& on history table: {str(history_table)}\n'
              f'apk url: {no_ext_url+".apk" if no_ext_url else ""}\n' + '-'*20)
        print('history update of \n [history_table, app_id, build_request_id, version_name, app_version]: \n',
              str([history_table, app_id, build_request_id, version_name, version_num]))
        print(f'ENDPOINT: build status update > of id: {build_request_id} to status: {update_status}')

        reply = {
            'status': True,
            'message': 'build status updated',
            'build_request_id': build_request_id,
            'update_status': update_status,
            'update_status_message': build_status_options.mapper.get(int(update_status)),
            'app_id': app_id,
            'app_platform': platform_options.mapper[int(platform_id)]
        }

        return JsonResponse(reply) if request else reply

platform_options = BuildStatusManager.DATA.Platform
build_status_options = BuildStatusManager.DATA.BuildStatus

@csrf_exempt
def get_make(request):
    app_id = str(request.POST.get('app_id'))
    user_id = str(request.POST.get('user_id'))
    req_build_platform = str(request.POST.get('build_platform'))
    version_name = str(request.POST.get('version_name') or 'App Name (default)')
    print("hello")
    # DATA PRE-CHECK ---------------------------------------------------------------------------------------------------
    if app_id == "0":
        print('requested app_id 0\nsample app_data currently unavailable...')
        return JsonResponse({
            'status': False,
            'message': "build request failed!\nInvalid app_id 0"
        })

    if req_build_platform not in platform_options.mapper.values():
        print('warning: no calls to android or ios made (check endpoint platform variable)')
        return JsonResponse({
            'status': False,
            'message': "Bad request, build request failed!\nInvalid platform: " + req_build_platform,
            'data': {
                "build_app_id": app_id,
                "build_platform": req_build_platform
            }
        })
    else:
        for key_pf_id, value_pf_name in platform_options.mapper.items():
            if req_build_platform == value_pf_name:
                req_build_platform = key_pf_id
                break
    

    # CREATE BUILD ENTRY (add build entry to db and gets build id/number)
    build_id = BuildStatusManager.create_build_status(req_build_platform, app_id, version_name, user_id or 9741)

    # CALL APP BUILDER as thread
    connections.close_all()
    worker = multiprocessing.Process(target=app_worker_thread, args=(app_id, req_build_platform, build_id))
    worker.name = f'app-{app_id}_build-{build_id}_workload'
    worker.start()

    # PREP & SEND MAKE (Endpoint) RESPONSE
    build_status = build_status_options.ONGOING
    build_response = build_status_options.get_response_json_basic(build_status, build_id, app_id, req_build_platform)
    build_response['message'] = "build request initiated"
    return JsonResponse(build_response)

def app_worker_thread(app_id, req_build_platform, build_id):
    # GET APP_DATA [DB -> JSON] ----------------------------------------------------------------------------------------
    print('*' * 50)
    print(f'\n\nMAKE APP [{app_id}] ')
    print('starting build process with build_id: ' + str(build_id))
    print("\n" * 2 + "-" * 25 + " AppData " + "-" * 25 + "\n")
   # connection to db----------
    # cursor = connection.cursor()
    # cursor.execute("SELECT app_details FROM app_factory_application WHERE application_id=%s", [app_id])
    # WARNING: Add app not found case and send it as json error response
    # app_data = cursor.fetchone()[0]
    try:
        # print('APP_DATA JSON: ' + str(app_data))
        # app_data = json.loads(app_data)
        # base.ProcessAppData(app_data)

        # Connection only with json-----------

        with open(r'D:\AppFactoryBack_end\AppFactoryDjango\AppfactoryApp\json_file.py') as f:
          app_data = json.load(f)
        #   print(app_data)
          base.ProcessAppData(app_data)
    except Exception as error:
        error_msg = str(error)
        print('json parse error: ' + error_msg)

    print("\n" + "=" * 60 + "\n" * 3)

class Extras:
    @staticmethod
    def ping(request):
        return HttpResponse("ping ok")



        


            



# Create your views here.
