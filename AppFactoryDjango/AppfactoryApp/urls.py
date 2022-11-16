from django.contrib import admin
from django.urls import path, include

from .import views



urlpatterns = [
    path(
        'ultimate-appfactory/make',
         views.get_make
    ),
    path(
        'ultimate-appfactory/build_status/get/by_app_id/<str:req_build_platform>/<int:app_id>',
         views.BuildStatusManager.view_status_by_app
    ),
    path(
        'ultimate-appfactory/build_status/get/by_build_id/<str:build_id>',
         views.BuildStatusManager.view_status_by_build_id
    ),
    path(
        'ultimate-appfactory/build_status/update/by_build_id',
         views.BuildStatusManager.update_status_by_build_id
    ),
    path(
        'ping',
         views.Extras.ping
    ),

]

 