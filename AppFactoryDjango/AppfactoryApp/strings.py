# --------------KIVY FILE STRINGS--------------------------#

screen_string = """
AnchorLayout:
    # apply padding top which is equal to height of tab bar
    padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]
    # padding top will be 0 if no tab bar      #screen padding
    anchor_x:'<<<horizontal_align>>>'                  #screen horizontal alignment
    anchor_y:'<<<vertical_align>>>'                    #screen vertical alignment
    canvas:
        Color:
            rgba:<<<bg_color>>>                         #screen background color
        Rectangle:
            pos:self.pos
            size:(app.window_width, app.window_height-<<<tab_bar_height>>>-<<<app_bar_height>>>)  # (800,600) without tabbar
            #<<<screen_background_image>>>             #screen background image
    MDBoxLayout:
        id:<<<screen_id>>>
        orientation:'vertical'
        adaptive_height: True
        adaptive_width: True   
"""

horizontal_layout_kivy_string = """
ClickableBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint: None, None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height

    ScrollView:
        do_scroll_x:False
        do_scroll_y:False
        size_hint: None, None
        size: dp(<<<width>>>),dp(<<<height>>>)                                               #width, height
        AnchorLayout:
            padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
            anchor_x:"<<<horizontal_alignment>>>"                                              #Horizontal alignment
            anchor_y:"<<<vertical_alignment>>>"                                               #vertical alignment
            size_hint: None, None
            size: dp(<<<width>>>),dp(<<<height>>>)                                               #width, height
            canvas:
                Color:
                    rgba:hex('<<<bg_color>>>')                                   #layout background color1
                Rectangle:
                    pos:self.pos
                    size:self.size

            MDBoxLayout:
                id:<<<layout_id>>>
                padding:[dp(0), dp(0), dp(0), dp(0)]                                             
                # md_bg_color:rgba("#e65f29")
                pos_hint:{'x':0,'top':1}
                adaptive_height:True
                adaptive_width:True
"""

vertical_layout_kivy_string = """
ClickableBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint: None, None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height

    ScrollView:
        do_scroll_x:False
        do_scroll_y:False
        size_hint: None, None
        size: dp(<<<width>>>),dp(<<<height>>>)                                               #width, height
        AnchorLayout:
            padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
            anchor_x:"<<<horizontal_alignment>>>"                                              #Horizontal alignment
            anchor_y:"<<<vertical_alignment>>>"                                               #vertical alignment
            size_hint: None, None
            size: dp(<<<width>>>),dp(<<<height>>>)                                               #width, height
            canvas:
                Color:
                    rgba:hex('<<<bg_color>>>')                                   #layout background color1
                Rectangle:
                    pos:self.pos
                    size:self.size

            MDBoxLayout:
                id:<<<layout_id>>>
                orientation:'vertical'
                padding:[dp(0), dp(0), dp(0), dp(0)]                                             
                # md_bg_color:rgba("#e65f29")
                pos_hint:{'x':0,'top':1}
                adaptive_height:True
                adaptive_width:True
"""

card_view_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint: None, None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height

    MDCard:
        id:card1
        padding:[<<<border_size>>>]                                    #border size
        md_bg_color:rgba('<<<border_color>>>')                        #border color
        radius:[<<<border_radius>>>]                                  #border radius 1
        size_hint:None,None
        size:dp(<<<width>>>),dp(<<<height>>>)         #width, height2 #adjust box1 size
        MDCard:
            id:<<<action_id>>>
            padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)] 
            md_bg_color:rgba("<<<bg_color>>>")                         #bg color
            radius:[<<<border_radius>>>]                         #border radius 2
            pos_hint: {'x':0, 'top':1}
            ScrollView:
                do_scroll_x:False
                do_scroll_y:False
                adaptive_size:True
                AnchorLayout:
                    anchor_x:"<<<horizontal_alignment>>>"                 #halign
                    anchor_y:"<<<vertical_alignment>>>"                   #valign
                    MDBoxLayout:
                        id:<<<layout_id>>>
                        orientation:'vertical'
                        adaptive_size: True
"""

button_kivy_string = """
#:import utils kivy.utils
ClickableBoxLayout:
    id:box1
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    #<<<pos_hint_marking>>>
    size_hint:None,None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    Shadow:
        padding:[dp(0), dp(0), dp(0), dp(0)] 
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        soft_shadow_cl:rgba('<<<shadow_color>>>')
        radius:[dp(<<<border_radius>>>)]  

        MDCard:
            padding:[2]                                                         #border size
            md_bg_color: rgba("<<<border_color>>>")                    #border color
            radius:[dp(<<<border_radius>>>)]                                                           #border radius 1
            size_hint:None,None
            size:(dp(<<<width>>>), dp(<<<height>>>))         # adjust with border size                                    
            # adaptive_height:True
            # adaptive_width:True
            MDCard:
                id:<<<action_id>>>
                padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]
                md_bg_color: rgba("<<<bg_color>>>")                #bg color
                radius:[dp(<<<border_radius>>>)]                  #border radius 2
                pos_hint: {'x':0, 'top':1}
                <<<bg_image>>>                               # bg image

                MDLabel:
                    text: '<<<text>>>'                           #text
                    bold: True
                    font_size: '<<<font_size>>>'                       #font size
                    font_name: 'fonts/<<<font_type>>>'    #font type
                    color: rgba("<<<font_color>>>")                     #text color
                    halign:"<<<text_alignment>>>"                           #text alignment
                    #md_bg_color: rgba("#cf8f522")                                        #bg color

"""

text_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    ClickableBoxLayout:
        id:<<<action_id>>>
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]
        size_hint:(None, None)
        size:(dp(<<<width>>>), dp(<<<height>>>))  # width, height
        md_bg_color:rgba("<<<bg_color>>>")
        orientation:'vertical'

        MDLabel:
            text: '<<<text>>>'                           #text
            bold: True
            font_size: '<<<font_size>>>'                       #font size
            font_name: 'fonts/<<<font_type>>>'    #font type
            color: rgba("<<<font_color>>>")                     #text color
            halign:"<<<text_alignment>>>"                           #text alignment
            #md_bg_color: rgba("#cf8f522")                                        #bg color
"""

text_field_kivy_string = """
MDBoxLayout:
    id:box1
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:None,None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                     #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    Shadow:
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        soft_shadow_cl:rgba('<<<shadow_color>>>')
        radius:[dp(<<<border_radius>>>)]  
        MDCard:
            id:card1
            padding:[5]                                                         #border size
            md_bg_color: rgba("#3cdec8")                    #border color
            radius:[5]                                                         #border radius 1
            size_hint:None,None
            size:(dp(<<<width>>>), dp(<<<height>>>))                                             #width, height2 #adjust box1 size
            MDCard:
                id:card2
                padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]
                # md_bg_color: rgba("#e8e582")                                        #bg color
                radius:[5]                                                     #border radius 2
                pos_hint: {'x':0, 'top':1}
                MDTextField:
                    id:<<<action_id>>>
                    text:'<<<hint_text>>>'
                    font_size: '<<<font_size>>>'                       #font size
                    font_name: 'fonts/<<<font_type>>>'    #font type
                    text_color: rgba("<<<font_color>>>")                     #text color
                    halign:"<<<text_alignment>>>"                           #text alignment
                    input_type:"<<<input_type>>>"
                    current_hint_text_color:rgba("<<<hint_text_color>>>")   # Hint text color
                    # input_filter:'int'
                    size_hint:(None,None)
                    size:(dp(<<<width>>>), dp(<<<height>>>))             #width
                    valign:'center'
"""

# button_kivy_string = """
# #:import utils kivy.utils
# MDBoxLayout:
#     id:box1
#     padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]
#     adaptive_size:True
#     # size_hint:None,None
#     # size:(dp(200), dp(50)) #card1 size + box1 padding
#     Shadow:
#         padding:[dp(0), dp(0), dp(0), dp(0)]
#         pos_hint: {'center_x': .5, 'center_y': .5}
#         adaptive_height:True
#         adaptive_width:True
#         shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20))
#         elevation: <<<shadow_blur>>> #blur
#         radius:[dp(<<<border_radius>>>)]
#         soft_shadow_cl:rgba('<<<shadow_color>>>')
#
#
#         MDCard:
#             id:card1
#             padding:[5]                                                         #border size
#             md_bg_color: rgba("<<<border_color>>>")                    #border color
#             radius:[dp(<<<border_radius>>>)]                          #border radius 1
#             size_hint:None,None
#             size:(dp(<<<width>>>), dp(<<<height>>>))         # adjust with border size
#             # adaptive_height:True
#             # adaptive_width:True
#             MDCard:
#                 id:card2
#                 padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]
#                 md_bg_color: rgba("<<<bg_color>>>")                                        #bg color
#                 radius:[dp(<<<border_radius>>>)]                                                     #border radius 2
#                 pos_hint: {'x':0, 'top':1}
#                 #<<<bg_image>>>                               # bg image
#
#                 MDLabel:
#                     text: '<<<text>>>'                           #text
#                     bold: True
#                     font_size: '<<<font_size>>>'                       #font size
#                     font_name: 'fonts/<<<font_type>>>'    #font type
#                     color: rgba("<<<font_color>>>")                     #text color
#                     halign:"<<<text_alignment>>>"                           #text alignment
#                     #md_bg_color: rgba("#cf8f522")                                        #bg color
# """

date_picker_string = """
MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    adaptive_height: True
    adaptive_width:True
    # size_hint:(None, None)
    # size:(dp(210),dp(60))     # height adjust size with border 
    Shadow:
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_x>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  
        soft_shadow_cl:rgba('<<<shadow_color>>>')

        #for border
        MDCard
            padding:[dp(<<<border_size>>>)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:date_picker_id
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                padding:[dp(0), dp(0), dp(0), dp(0)]  #padding
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    

                    MDIcon:
                        id:date_picker_icon
                        icon:"calendar"
                        theme_text_color:'Custom'
                        text_color:[0, 0, .5, .7]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 

                    Label:
                        id:date_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height
"""

image_picker_kivy_string = """
MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    Shadow:
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  
        soft_shadow_cl:rgba('<<<shadow_color>>>')
        #for border
        MDCard
            padding:[dp(0)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:image_picker_id
                padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]      #padding
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                padding:[dp(0), dp(0), dp(0), dp(0)]  #padding
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    

                    MDIcon:
                        id:image_picker_icon
                        icon:"image"
                        theme_text_color:'Custom'
                        text_color:[1, 1, .5, 1]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 
                        pos_hint: {'center_x': .5, 'center_y': .5}

                    Label:
                        id:image_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height
"""

table_layout_kivy_string = """
ClickableBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint: None, None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                     #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    AnchorLayout:
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        anchor_x:"<<<horizontal_alignment>>>"                                              #Horizontal alignment
        anchor_y:"<<<vertical_alignment>>>"                                               #vertical alignment
        size_hint: None, None
        size: dp(<<<width>>>),dp(<<<height>>>)                                               #width, height
        MDGridLayout:
            adaptive_height: True
            adaptive_width: True
            id:<<<layout_id>>>
            padding: [0, 0, 0, 0]  # padding
            rows: <<<row>>>  # table row
            cols: <<<col>>>  # table col
            # size_hint: None, None
            # size: dp(300),dp(200)  # width, height
            spacing: 2
            # spacing:[5,0]
            orientation: 'lr-tb'    
            # md_bg_color:rgba("#e65f29")                                                    
"""

# card_view_kivy_string = """
# MDBoxLayout:
#     id:outer_layout
#     padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]
#     adaptive_size:True
#     MDCard:
#         id:card1
#         padding:[<<<border_size>>>]                                                         #border size
#         md_bg_color:rgba('<<<border_color>>>')                                      #border color
#         radius:[<<<border_radius>>>]                                                        #border radius 1
#         size_hint:None,None
#         size:dp(<<<width>>>),dp(<<<height>>>)                                             #width, height2 #adjust box1 size
#         MDCard:
#             id:action_id
#             padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
#             md_bg_color:rgba("<<<bg_color>>>")                                        #bg color
#             radius:[<<<border_radius>>>]                                                     #border radius 2
#             pos_hint: {'x':0, 'top':1}
#             AnchorLayout:
#                 anchor_x:"<<<horizontal_alignment>>>"                                             #halign
#                 anchor_y:"<<<horizontal_alignment>>>"                                              #valign
#                 MDBoxLayout:
#                     orientation:'vertical'
#                     size_hint:None,None
#                     size:(dp(50), dp(100)) #card1 size + box1 padding
#
#                     # Button:
#                     #     text:"Button"
#                     #     size_hint:None,None
#                     #     size:(dp(50), dp(50))
#                     # Button:
#                     #     text:"Button"
#                     #     size_hint:None,None
#                     #     size:(dp(50), dp(50))
# """

webview_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                               
    adaptive_height:True
    adaptive_width:True
    # md_bg_color:[1, .1, .8, 1]

    AnchorLayout:
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        # adaptive_height:True
        # adaptive_width:True
        size_hint:(None, None)
        size:(dp(<<<width>>>), dp(<<<height>>>))  # width, height
        canvas:
            Color:
                rgba:hex("<<<bg_color>>>")                                              
            Rectangle:
                pos:self.pos
                size:self.size

        MDBoxLayout:
            id:webview_id
            adaptive_height:True
            adaptive_width:True
            md_bg_color:[1, 1, .8, 1]
            pos_hint:{'center_x':0.5,'center_y':0.5}

            MDIconButton:
                icon: "web"
                theme_text_color: 'Custom'
                text_color: [0,0,.5,.7]             #icon color
                pos_hint:{'center_x':0.5,'center_y':0.5}
"""
list_viewer_kivy_string = """
MDGridLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                               
    adaptive_height:True
    adaptive_width:True
    spacing:1
    cols:1
    #<<<new_list_item_marking>>>
"""

list_item_kivy_string = """
    MDCard:
        id:list<<<count>>>_id
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        md_bg_color:rgba('<<<bg_color>>>')
        size_hint:(None, None)
        size:(dp(<<<width>>>), dp(<<<height>>>))  #width, height 1
    
        Label:
            text:'<<<text>>>'  # text
            font_size:'<<<font_size>>>'  # font size
            font_name:'fonts/<<<font_type>>>'  # font type
            color:rgba('<<<font_color>>>')  # list color
            pos_hint:{'x': 0, 'top': 1}
            size_hint:(None, 1)
            # size_hint:(None, None)
            # size:(dp(250), dp(40))  
            text_size:self.size
            valign:'center'

"""
tab_navigator_kivy_string = """
AnchorLayout:
    padding:[dp(0), dp(0), dp(0), dp(0)]                                            
    anchor_x:"left"                                                         
    anchor_y:"top"                                                          

    MDBoxLayout:
        id:grid
        cols:3  # no.of tabs
        padding:[dp(0), dp(0), dp(0), dp(0)] 
        size_hint: None, None
        size: (app.window_width, 50)                #tabbar height 50px - adjust screen padding and size 
        canvas:
            Color:
                rgba:<<<bg_color>>>               # tabbar bg-color
            Rectangle:
                pos:self.pos
                size:self.size
                #source:'img.jpg'
        #<<<new_tab_marking>>>

"""
tab_string = """
        MDBoxLayout:
            orientation:"vertical"
            Button:
                id:<<<tab_bar_id>>>
                text:'<<<text>>>'  # text
                font_size:'<<<font_size>>>'  # font size
                font_name:'fonts/<<<font_type>>>'  # font type
                color:rgba('<<<font_color>>>')  # list color
                pos_hint:{'x': 0, 'top': 1}
                text_size:self.size
                valign:'center'
                background_normal:''
                background_color:(.1,1,1,1)
            MDCard:
                id:<<<tab_id>>>
                size_hint:None,None
                size: (250,5)
                md_bg_color:(.1, 1, .1, .4)
"""

time_picker_kivy_string = """
MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    Shadow:
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  
        soft_shadow_cl:rgba('<<<shadow_color>>>')
        #for border
        MDCard
            padding:[dp(0)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:time_picker_id
                padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]      #padding
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    

                    MDIcon:
                        id:time_picker_icon
                        icon:"clock"
                        theme_text_color:'Custom'
                        text_color:[1, 1, .5, 1]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 
                        pos_hint: {'center_x': .5, 'center_y': .5}

                    Label:
                        id:time_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height
"""
date_picker_kivy_string = """
MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    Shadow:
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  
        soft_shadow_cl:rgba('<<<shadow_color>>>')
        #for border
        MDCard
            padding:[dp(0)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:date_picker_id
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    
                    pos_hint: {'center_x': .5, 'center_y': .5}

                    MDIcon:
                        id:date_picker_icon
                        icon:"calendar"
                        theme_text_color:'Custom'
                        text_color:[0, 0, .5, .7]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 
                        pos_hint: {'center_x': .5, 'center_y': .5}
                    Label:
                        id:date_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height
"""
app_bar_kivy_string="""
MDBoxLayout:
    size_hint : (None, None)
    size : (app.window_width, 50)
    pos_hint: {'x': 0, 'top': 1}

    MDBoxLayout:
        padding:[0, 0, 0, 0]
        size_hint:(None, None)
        size:(app.window_width, 50)                                 
        md_bg_color:rgba('<<<bg_color>>>') 
        MDIconButton:
            id:app_bar_id
            padding:[0, 0, 0, 0]
            icon:"arrow-left"
            theme_text_color:'Custom'
            text_color:rgba('#ffffff')                     # icon color
        # AnchorLayout:
        #     padding:[0,0,0,0]
        #     pos_hint:{'x': .5, 'top': 1}
        #     size_hint:(None, None)
        #     size:(app.window_width-appbar_icon.width, 50)
        #     anchor_x:'center'                             # text alignment 1
        #     anchor_y:'top'
        Button:
            id:button2
            text:'<<<text>>>'  # text
            font_size:'<<<font_size>>>px'  # font size
            font_name:'fonts/<<<font_family>>>'  # font type
            color:rgba('<<<font_color>>>')  # tab color
            pos_hint:{'x': 0, 'top': 1}
            text_size:self.size
            valign:'center'
            halign:'<<<text_alignment>>>'
            background_normal:''
            background_color:rgba('<<<bg_color>>>') 

"""
image_auto_kivy_string = """
#:import utils kivy.utils
MDBoxLayout:
    id:box1
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint: None, None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    # md_bg_color: 1, .1, 1, .1
    MDBoxLayout:
        id:box1
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        adaptive_size:True
        Shadow:
            pos_hint: {'center_x': .5, 'center_y': .5}
            adaptive_height:True
            adaptive_width:True
            shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
            elevation: <<<shadow_blur>>> #blur
            md_bg_color: 1, 1, 1, 1
            radius:[dp(<<<border_radius>>>)]  
            soft_shadow_cl:rgba('<<<shadow_color>>>')
            MDCard:
                id:card2
                # md_bg_color: rgba("#e8e582")
                radius:[5]
                pos_hint: {'x':0, 'top':1}
                size_hint:(None, None)
                size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

                #<<<image-marking>>>

"""


image_contain_kivy_string = """
MDBoxLayout:
    id:box1
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint: None, None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    MDBoxLayout:
        id:box1
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        size_hint:None,None
        size:(dp(<<<width>>>), dp(<<<height>>>))

        Shadow:
            pos_hint: {'center_x': .5, 'center_y': .5}
            adaptive_height:True
            adaptive_width:True
            shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
            elevation: <<<shadow_blur>>> #blur
            md_bg_color: 1, 1, 1, 1
            radius:[dp(<<<border_radius>>>)]  
            soft_shadow_cl:rgba('<<<shadow_color>>>')
            MDCard:
                id:card2
                # md_bg_color: rgba("#e8e582")
                radius:[dp(<<<border_radius>>>)]
                pos_hint: {'x':0, 'top':1}
                size_hint:None,None
                size:(dp(<<<width>>>), dp(<<<height>>>))

                Image:
                    #<<<image-marking>>>
                    #radius: [25]
                    allow_stretch: True

"""

image_cover_kivy_string = """
MDBoxLayout:
    id:box1
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint: None, None
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    MDBoxLayout:
        id:box1
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        size_hint:None,None
        size:(dp(<<<width>>>), dp(<<<height>>>))

        Shadow:
            pos_hint: {'center_x': .5, 'center_y': .5}
            adaptive_height:True
            adaptive_width:True
            shadow_pos: dp(<<<shadow_x>>>) + dp(0), dp(-<<<shadow_y>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
            elevation: <<<shadow_blur>>> #blur
            md_bg_color: 1, 1, 1, 1
            radius:[dp(<<<border_radius>>>)]  
            soft_shadow_cl:rgba('<<<shadow_color>>>')
            MDCard:
                id:card2
                # md_bg_color: rgba("#e8e582")
                radius:[dp(<<<border_radius>>>)]
                pos_hint: {'x':0, 'top':1}
                size_hint:None,None
                size:(dp(<<<width>>>), dp(<<<height>>>))

                FitImage:
                    #<<<image-marking>>>
                    radius:[dp(<<<border_radius>>>)]
                    allow_stretch: True

"""
switch_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        id:box_padding
        padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
        size_hint:(None, None)
        size:(dp(200), dp(100))  # width, height
        md_bg_color:[1, 1, .8, 1]
        orientation:'vertical'
        MDBoxLayout:
            padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
            adaptive_height:True
            adaptive_width:True
            # md_bg_color:[1, 1, .1, 1]
            MDSwitch:
                widget_style: "ios"
                theme_thumb_color: "Custom"
                thumb_color_active: 1, 0, 0, 1
                thumb_color_inactive: 1, 0, 1, 1
                track_color_active: (1,0,1,1)
                track_color_inactive: (1,1,0,1)
            Label:
                text:'Check box1'  # button
                font_size:'15px'  # font size
                font_name:'font/ShortBaby-Mg2w.ttf'  # font type
                color:(1, 0, .1, 1)  # font color
                size_hint:(None,None)
                size:(dp(150),dp(50))
                text_size:self.size
                halign:"left"  # text alignment
                valign:'center'
"""
check_box_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        id:box_padding
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        size_hint:(None, None)
        size:(dp(200), dp(50))  # width, height
        md_bg_color:[1, 1, .8, 1]
        orientation:'vertical'
        MDBoxLayout:
            padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
            adaptive_height:True
            adaptive_width:True
            # md_bg_color:[1, 1, .1, 1]

            MDCheckbox:
                selected_color:rgba('<<<active_color>>>') # active color
                unselected_color:rgba('<<<inactive_color>>>') # inactive color
                active:True
                # checkbox_icon_down:'circle-slice-8'
                allow_no_selection:False
                size_hint:(None,None)
                size:(dp(50),dp(50))
            Label:
                text:'<<<text>>>'  # button
                font_size:'<<<font_size>>>px'  # font size
                font_name:'fonts/<<<font_type>>>'  # font type
                color:rgba('<<<font_color>>>')  # font color
                size_hint:(None,None)
                size:(dp(150),dp(50))
                text_size:self.size
                halign:"left"  # text alignment
                valign:'center'
"""

audio_picker_kivy_string = """
MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    Shadow:
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(-<<<shadow_x>>>) + dp(20), dp(-<<<shadow_x>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  

        #for border
        MDCard
            padding:[dp(2)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:date_picker_id
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    

                    MDIcon:
                        id:date_picker_icon
                        icon:"calendar"
                        theme_text_color:'Custom'
                        text_color:[0, 0, .5, .7]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 

                    Label:
                        id:date_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height
"""

video_picker_kivy_string = """
MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    Shadow:
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(-<<<shadow_x>>>) + dp(20), dp(-<<<shadow_x>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  

        #for border
        MDCard
            padding:[dp(2)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:date_picker_id
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    

                    MDIcon:
                        id:date_picker_icon
                        icon:"calendar"
                        theme_text_color:'Custom'
                        text_color:[0, 0, .5, .7]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 

                    Label:
                        id:date_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height
"""

video_player_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        adaptive_height: True
        adaptive_width: True
        md_bg_color:[1,.9,.1,1]                  #bg color
        Shadow:
            padding:[dp(0), dp(0), dp(0), dp(0)] 
            pos_hint: {'center_x': .5, 'center_y': .5}
            adaptive_height:True
            adaptive_width:True
            shadow_pos: dp(-<<<shadow_x>>>) + dp(20), dp(-<<<shadow_x>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
            elevation: <<<shadow_blur>>> #blur
            md_bg_color: 1, 1, 1, 1
            radius:[dp(<<<border_radius>>>)]  
            MDBoxLayout:
                orientation:'vertical'
                size_hint:None,None
                pos_hint: {'center_x': .5, 'center_y': .5}
                size:dp(<<<width>>>),dp(<<<height>>>)                              #width, height
                md_bg_color:[.1,.1,.1,1]                  #bg color
                Videos:
                    pos_hint_y:{'y':0}
                    id:video
                    source:'videos/<<<video_file>>>'
                    state:'pause'
    
                MDBoxLayout:
                    size_hint:None,None
                    size:dp(250),dp(40)                              #width, height
                    md_bg_color:[.1,.1,.1,1]                  #bg color
    
                    MDIconButton:
                        id:play_id
                        icon: "play"
                        theme_text_color: 'Custom'
                        text_color: [1,1,1,1]             #icon color
                    MDLabel:
                        id:current_time
                        text:"00:00 / 00:00"
                        font_size:11
                        color:[1,1,1,1]
                    MDSlider:
                        id:volume_slider_id
                        min: 0
                        max: 1
                        value: .4
                        hint: False
                        color: [1,1,1,1]
                        # on_value: volume(self,self.value)
                    MDIconButton:
                        id:volume_id
                        icon: "volume-high"
                        theme_text_color: 'Custom'
                        text_color: [1,1,1,1]
    
                    MDIconButton:
                        id:dots_id
                        icon: "dots-vertical"
                        theme_text_color: 'Custom'
                        text_color: [1,1,1,1]
    
    
                    # MDIconButton:
                    #     icon: "download"
                    #     theme_text_color: 'Custom'
                    #     text_color: [1,1,1,1]
                MDBoxLayout:
                    size_hint:None,None
                    size:dp(250),dp(20)                              #width, height
                    md_bg_color:[.1,.1,.1,.3]                  #bg color
                    MDSlider:
                        id:progressbar
                        max:100
                        value:0
                        color: [1,1,1,1]
                    # MDProgressBar:
                    #     id:progressbar
                    #     max:100
                    #     value:0
                    #     color: (1,.1,.1,.7)
                    #     size_hint:None,None
                    #     height:dp(20)  
                    #     width:root.width-40
                    #     pos_hint:{'center_x':0.5,'top':1} 
                    #     on_touch_move:
                    #         if self.collide_point(args[1].pos[0], args[1].pos[1]): \
                    #             self.value = round(((args[1].pos[0]-20)/self.width)*100);
                    #     Thumb:
                    #         size_hint:None,None
                    #         size:"15dp","15dp"
                    #         pos:progressbar.pos
                    #         # pos: (progressbar.value*progressbar.width)/100+20, progressbar.center_y - self.height/2 - dp(2)
                    #         color: progressbar.color
"""

audio_picker_main_string = """
   def file_select(self,*args):
        file_name = filechooser.open_file(filters=[("*.mp3")])
        print(file_name)
        # self.ids.image11.source=file_name[0]
        # self.ids.video11.source=file_name[0]



"""
map_view_kivy_string = """
MDBoxLayout:
    padding:dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)
    adaptive_height: True
    adaptive_width: True
    size_hint:None,None
    size:<<<width>>>,<<<height>>>
    #md_bg_color:[1,.3,1,1]
    AnchorLayout:
        padding:dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)
        #:import MapView kivy_garden.mapview.MapView
        MapView:
            zoom:10
            id:map1
            lat:8.5581
            lon:76.8816
            size_hint:(None,None)
            width:dp(<<<width>>>)
            height:dp(<<<height>>>)
"""
audio_player_kivy_string = """
MDBoxLayout:
    padding:dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)
    # size_hint:(None, None)
    # size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    adaptive_height: True
    adaptive_width: True

    MDBoxLayout:
        padding:dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)
        adaptive_height: True
        adaptive_width: True
        # md_bg_color:[1,.9,.1,1]                  #bg color
        MDBoxLayout:
            size_hint:None,None
            # pos_hint: {'center_x': .5, 'center_y': .5}
            size:dp(<<<width>>>),dp(<<<height>>>)                              #width, height
            md_bg_color:[1,.9,1,1]                  #bg color
            radius:[25]
            MDIconButton:
                id:play_id
                icon: "play"
                theme_text_color: 'Custom'
                text_color: [.1,.1,.1,4]             #icon color

            MDProgressBar:
                size_hint:None,None
                size:40,5                             
                id:progressbar
                max:100
                value:0
                color: (1,1,.1,1)
                back_color:(.1,1,1,1)
                pos_hint:{"center_y":0.5}
            MDLabel:
                id:current_time
                text:" 00:00 / 0:00"
                font_size:11
                size_hint:None,None
                size:70,5       
                pos_hint:{"center_y":0.5}                 
            MDSlider:
                id:volume_slider_id
                min: 0
                max: 1
                value: .4
                hint: False
                color: app.theme_cls.accent_color
                # on_value: volume(self,self.value)
                size_hint:None,None
                size:60,5       
                pos_hint:{"center_y":0.5}                 
            MDIconButton:
                id:volume_id
                icon: "volume-high"
                theme_text_color: 'Custom'
                text_color: [0,0,.5,.7]

            #MDIconButton:
                #icon: "dots-vertical"
                #theme_text_color: 'Custom'
                #text_color: [0,0,.5,.7]

            MDIconButton:
                id:download_id
                icon: "download"
                theme_text_color: 'Custom'
                text_color: [0,0,.5,.7]
                ripple_scale: 8
"""

slider_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                             #margin
    size_hint:(None, None)
    size:(dp(<<<width>>>), dp(<<<height>>>))  # margin + box_padding size
    adaptive_height:True
    adaptive_width:True
    MDBoxLayout:
        id:box_padding
        padding:dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)                       #padding
        size_hint:(None, None)
        size:(dp(<<<width>>>), dp(<<<height>>>))  # width, height
        md_bg_color:[1, 1, .8, 1]
        orientation:'vertical'
        MDBoxLayout:
            padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
            adaptive_height:True
            adaptive_width:True
            # md_bg_color:[1, 1, .1, 1]

        MDBoxLayout:
            pos_hint:{'x': 0, 'center_y': 0.5}
            adaptive_height:True
            adaptive_width:True
            # md_bg_color:[1, 1, .1, 1]

            MDSlider:
                min: 0
                max: 100
                # color: (1, 0, 1, 1)  ###########left color
                track_color_active: rgba('<<<active_track_color>>>')  #####right color
                track_color_inactive:rgba('<<<inactive_track_color>>>') ######right color
                thumb_color_active: rgba('<<<active_thumb_color>>>')  #####thumb color
                size_hint:(None, None)
                size:(dp(200), dp(100))  # width, height

"""
camera_kivy_string = """

MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    adaptive_height: True
    adaptive_width:True
    # size_hint:(None, None)
    # size:(dp(210),dp(60))     # height adjust size with border 
    Shadow:
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(-<<<shadow_x>>>) + dp(20), dp(-<<<shadow_x>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  

        #for border
        MDCard
            padding:[dp(<<<border_size>>>)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:date_picker_id
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                padding:[dp(0), dp(0), dp(0), dp(0)]  #padding
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    

                    MDIcon:
                        id:date_picker_icon
                        icon:"camera"
                        theme_text_color:'Custom'
                        text_color:[0, 0, .5, .7]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 

                    Label:
                        id:date_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height

"""
barcode_scanner_kivy_string = """

MDBoxLayout:
    #for margin
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    adaptive_height: True
    adaptive_width:True
    # size_hint:(None, None)
    # size:(dp(210),dp(60))     # height adjust size with border 
    Shadow:
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]                                              #padding
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(-<<<shadow_x>>>) + dp(20), dp(-<<<shadow_x>>>) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: <<<shadow_blur>>> #blur
        md_bg_color: 1, 1, 1, 1
        radius:[dp(<<<border_radius>>>)]  

        #for border
        MDCard
            padding:[dp(<<<border_size>>>)] # border size - adjust parent size also
            md_bg_color:rgba("<<<border_color>>>")   # border color
            radius:[<<<border_radius>>>]  # border radius 1
            size_hint:(None, None)
            size:(dp(<<<width>>>),dp(<<<height>>>))    # height adjust size with border 

            MDCard:
                id:date_picker_id
                pos_hint:{'center_x':0.7, 'center_y': 0.5}
                padding:[dp(0), dp(0), dp(0), dp(0)]  #padding
                md_bg_color:rgba("<<<bg_color>>>")  # bg-color
                radius:[<<<border_radius>>>]      # border radius 2
                elevation:5
                # background:"images/img.jpg"
                MDBoxLayout:
                    orientation:'horizontal'
                    pos_hint:{'center_y':0.5}
                    adaptive_height: True
                    adaptive_width:True
                    # md_bg_color:[1, 1, .1, 1]
                    size_hint:(None, None)
                    size:(dp(200),dp(50))    

                    MDIcon:
                        id:date_picker_icon
                        icon:"scan"
                        theme_text_color:'Custom'
                        text_color:[0, 0, .5, .7]  # icon color
                        size_hint:(None, None)
                        size:(dp(40),dp(50))    # height adjust size with border 

                    Label:
                        id:date_picker_label
                        text:'<<<text>>>'  # button
                        font_size:'<<<font_size>>>'  # font size
                        font_name:'fonts/<<<font_type>>>'                    # font type
                        color:rgba('<<<font_color>>>')  # font color
                        #halign:"left"  # text alignment
                        pos_hint:{'x': 0, 'top': 1}
                        text_size:self.size
                        valign:'center'
                        size_hint : (None, None)
                        size : (dp(160),dp(50))  # width, height
"""
radio_button_kivy_string = """
MDBoxLayout:
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]  # margin
    size_hint:(None, None)
    size:(dp(200), dp(100))  # margin + box_padding size
    adaptive_height:True
    adaptive_width:True
    MDBoxLayout:
        id:box_padding
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]  # padding
        size_hint:(None, None)
        size:(dp(<<<width>>>), dp(<<<height>>>))  # width, height
        orientation:'vertical'
        MDBoxLayout:
            padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
            adaptive_height:True
            adaptive_width:True
            # md_bg_color:[1, 1, .1, 1]

            MDCheckbox:
                selected_color:[.1,1,1,1] # active color
                unselected_color:[.1,1,.1,.6] # active color
                group:'test'
                active:True
                radio_icon_down:'circle-slice-8'
                allow_no_selection:False
                size_hint:(None,None)
                size:(dp(50),dp(50))
            Label:
                text:'Radiobutton1'  # button
                font_size:'15px'  # font size
                #font_name:'font/ShortBaby-Mg2w.ttf'  # font type
                color:(1, 0, .1, 1)  # font color
                size_hint:(None,None)
                size:(dp(150),dp(50))
                text_size:self.size
                halign:"left"  # text alignment
                valign:'center'
"""
side_menu_kivy_string = """
GridLayout:
    cols:1
    MDTopAppBar:
        size_hint:(None,None)
        size:(dp(10),dp(20))
        id:toolbar
        md_bg_color:(1,.6,.6,1)
        opposite_colors:True
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    MDNavigationLayout:
        x: toolbar.height
        do_default_tab: False
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                nav_drawer: nav_drawer
                ScrollView:
                    MDGridLayout:
                        rows: 3
                        md_bg_color:(1,1,1,1)   # bg color
                        #<<<side_menu_tab_marking>>>
"""
side_menu_tabs_kivy_string="""
                        ClickableBoxLayout:
                            id:<<<tab_bar_id>>>
                            md_bg_color:rgba('<<<inactive_tab_color>>>')   # bg color
                            adaptive_size: True                            
                            # size_hint: None, None
                            # size: dp(300),dp(50)
                            MDLabel:
                                id:tab1
                                text: '<<<text>>>'                           #text
                                font_size: '<<<font_size>>>dp'                       #font size
                                #font_name: 'font/<<<font_type>>>'    #font type
                                color: 0, 0, 0, 1                       #text color
                                halign:"left"                           #text alignment
                                size_hint: None, None
                                size: dp(250),dp(50)
                            #<<<side_menu_icon_marking>>>
"""
side_menu_icon="""
                            MDIcon:
                                icon:'home'
                                size_hint: None, None
                                size: dp(50),dp(50)


"""
rating_bar_kivy_string = """
# for margin
MDBoxLayout:
    #: set ratingbar_icon 'star-outline'
    #: set icon_color_inactive [.1,1,1,1]
    #: set icon_color_active [1,0,0,1]
    
    id:box_padding
    # md_bg_color:[1, .1, 1, .1]
    padding:[dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)]                              
    size_hint:(None, None)
    size: dp(<<<width_margin_adj>>>),dp(<<<height_margin_adj>>>)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    AnchorLayout:
        id:anchor_padding    
        padding:[dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)]  # padding
        size_hint:(None, None)
        size:(dp(<<<width>>>), dp(50))  # width, height
        anchor_x:'center'
        anchor_y:'center'
        canvas:
            Color:
                rgba:(1,1,.8,1)                                                
            Rectangle:
                pos:self.pos
                size:self.size
                #source:'img.jpg'                                                
    
        ClickableBoxLayout:
            id:rating_id
            size_hint:(None, None)
            size : (dp(250), dp(50)) #fixed
            MDIconButton:
                id:icon_one
                icon:ratingbar_icon
                theme_text_color:'Custom'
                text_color:icon_color_inactive  # icon color
    
            MDIconButton:
                id:icon_two
                icon: ratingbar_icon
                theme_text_color:'Custom'
                text_color:icon_color_inactive  # icon color
    
            MDIconButton:
                
                id:icon_three
                icon: ratingbar_icon
                theme_text_color:'Custom'
                text_color:icon_color_inactive  # icon color
    
            MDIconButton:
                id:icon_four
                icon:ratingbar_icon
                theme_text_color:'Custom'
                text_color:icon_color_inactive  # icon color
    
            MDIconButton:
                id:icon_five
                icon: ratingbar_icon
                theme_text_color : 'Custom'
                text_color :icon_color_inactive  # icon color
"""

rating_bar_main_string = """
        # RATING BAR

        icon_color_inactive = '<<<inactive_color>>>'
        icon_color_active = '<<<active_color>>>'
        <<<rating_bar>>>.ids.icon_two.text_color = icon_color_inactive
        <<<rating_bar>>>.ids.icon_three.text_color = icon_color_inactive
        <<<rating_bar>>>.ids.icon_four.text_color = icon_color_inactive
        <<<rating_bar>>>.ids.icon_five.text_color = icon_color_inactive
        <<<rating_bar>>>.ids.icon_one.text_color = icon_color_inactive
        
        def select_star1(instance):
            <<<rating_bar>>>.ids.icon_two.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_three.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_four.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_five.text_color = icon_color_inactive

            if <<<rating_bar>>>.ids.icon_one.icon == 'star-outline':
                <<<rating_bar>>>.ids.icon_one.icon = 'star-half-full'
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_one.icon == 'star-half-full':
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
                <<<rating_bar>>>.ids.icon_one.icon = 'star'
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_one.icon == 'star':
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
                <<<rating_bar>>>.ids.icon_one.icon = 'star-outline'
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_two.icon = 'star-outline'
            <<<rating_bar>>>.ids.icon_three.icon = 'star-outline'
            <<<rating_bar>>>.ids.icon_four.icon = 'star-outline'
            <<<rating_bar>>>.ids.icon_five.icon = 'star-outline'

        def select_star2(instance):
            <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
            <<<rating_bar>>>.ids.icon_three.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_four.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_five.text_color = icon_color_inactive
            if <<<rating_bar>>>.ids.icon_two.icon == 'star-outline':
                <<<rating_bar>>>.ids.icon_two.text_color = icon_color_inactive
                <<<rating_bar>>>.ids.icon_two.icon = 'star-half-full'
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
                <<<rating_bar>>>.ids.icon_two.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_two.icon == 'star-half-full':
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
                <<<rating_bar>>>.ids.icon_two.text_color = icon_color_active
                <<<rating_bar>>>.ids.icon_two.icon = 'star'
                <<<rating_bar>>>.ids.icon_two.text_color = icon_color_active

            elif <<<rating_bar>>>.ids.icon_two.icon == 'star':
                <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
                <<<rating_bar>>>.ids.icon_two.text_color = icon_color_active
                <<<rating_bar>>>.ids.icon_two.icon = 'star-outline'
                <<<rating_bar>>>.ids.icon_two.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_one.icon = 'star'
            <<<rating_bar>>>.ids.icon_three.icon = 'star-outline'
            <<<rating_bar>>>.ids.icon_four.icon = 'star-outline'
            <<<rating_bar>>>.ids.icon_five.icon = 'star-outline'

        def select_star3(instance):
            <<<rating_bar>>>.ids.icon_four.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_five.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
            <<<rating_bar>>>.ids.icon_two.text_color = icon_color_active
            if <<<rating_bar>>>.ids.icon_three.icon == 'star-outline':
                <<<rating_bar>>>.ids.icon_three.text_color = icon_color_inactive
                <<<rating_bar>>>.ids.icon_three.icon = 'star-half-full'
                <<<rating_bar>>>.ids.icon_three.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_three.icon == 'star-half-full':
                <<<rating_bar>>>.ids.icon_three.icon = 'star'
                <<<rating_bar>>>.ids.icon_three.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_three.icon == 'star':
                <<<rating_bar>>>.ids.icon_three.icon = 'star-outline'
                <<<rating_bar>>>.ids.icon_three.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_one.icon = 'star'
            <<<rating_bar>>>.ids.icon_two.icon = 'star'
            <<<rating_bar>>>.ids.icon_four.icon = 'star-outline'
            <<<rating_bar>>>.ids.icon_five.icon = 'star-outline'

        def select_star4(instance):
            <<<rating_bar>>>.ids.icon_five.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_three.text_color = icon_color_active
            <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
            <<<rating_bar>>>.ids.icon_two.text_color = icon_color_active
            if <<<rating_bar>>>.ids.icon_four.icon == 'star-outline':
                <<<rating_bar>>>.ids.icon_four.icon = 'star-half-full'
                <<<rating_bar>>>.ids.icon_four.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_four.icon == 'star-half-full':
                <<<rating_bar>>>.ids.icon_four.icon = 'star'
                <<<rating_bar>>>.ids.icon_four.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_four.icon == 'star':
                <<<rating_bar>>>.ids.icon_four.icon = 'star-outline'
                <<<rating_bar>>>.ids.icon_four.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_one.icon = 'star'
            <<<rating_bar>>>.ids.icon_two.icon = 'star'
            <<<rating_bar>>>.ids.icon_three.icon = 'star'
            <<<rating_bar>>>.ids.icon_five.icon = 'star-outline'

        def select_star5(instance):
            <<<rating_bar>>>.ids.icon_four.text_color = icon_color_active
            <<<rating_bar>>>.ids.icon_three.text_color = icon_color_active
            <<<rating_bar>>>.ids.icon_one.text_color = icon_color_active
            <<<rating_bar>>>.ids.icon_two.text_color = icon_color_active
            if <<<rating_bar>>>.ids.icon_five.icon == 'star-outline':
                <<<rating_bar>>>.ids.icon_five.icon = 'star-half-full'
                <<<rating_bar>>>.ids.icon_five.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_five.icon == 'star-half-full':
                <<<rating_bar>>>.ids.icon_five.icon = 'star'
                <<<rating_bar>>>.ids.icon_five.text_color = icon_color_active
            elif <<<rating_bar>>>.ids.icon_five.icon == 'star':
                <<<rating_bar>>>.ids.icon_five.icon = 'star-outline'
                <<<rating_bar>>>.ids.icon_five.text_color = icon_color_inactive
            <<<rating_bar>>>.ids.icon_one.icon = 'star'
            <<<rating_bar>>>.ids.icon_two.icon = 'star'
            <<<rating_bar>>>.ids.icon_three.icon = 'star'
            <<<rating_bar>>>.ids.icon_four.icon = 'star'

        <<<rating_bar>>>.ids.icon_one.bind(on_press=select_star1)
        <<<rating_bar>>>.ids.icon_two.bind(on_press=select_star2)
        <<<rating_bar>>>.ids.icon_three.bind(on_press=select_star3)
        <<<rating_bar>>>.ids.icon_four.bind(on_press=select_star4)
        <<<rating_bar>>>.ids.icon_five.bind(on_press=select_star5)
"""


normal_modal_kivy_string = """
#:import Factory kivy.factory.Factory
<Mymodal@ModalView>:
    size:(50,20)
    size_hint:None,None
    BoxLayout:
        orientation:"vertical"
        width:dp(<<<width>>>)
        height:dp(<<<height>>>)
        padding:dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)     ###############margin of card
        size_hint:None,None
        canvas:
            Color:
                rgba:('<<<border_color>>>')    ##########color of border size
            Line:
                width:<<<border_size>>>          ###########border size
                rectangle: self.x, self.y, self.width, self.height
        ScrollView:
            orientation:"vertical"
            size_hint:(None,None)
            width:dp(<<<width>>>)
            height:dp(<<<height>>>)
            do_scroll_x:False
            do_scroll_y:True
            AnchorLayout:
                anchor_x:"left"
                anchor_y:"top"
                width:dp(<<<width>>>)
                height:dp(<<<height>>>)
                padding:dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)       #########padding of card
                canvas:
                    Color:
                        rgba:rgba('<<<bg_color>>>')       ###################color of modal background
                    Rectangle:
                        size:self.size
                        pos:self.pos
                GridLayout:
                    cols:1
                    size_hint: None, None
                    size: self.minimum_size
                    pos_hint: {'top': 1}
                    canvas.before:
                        Color:
                            rgba:(0,0,0,0)
                        Rectangle:
                            pos:self.pos
                            size:self.size
"""


##--------------PYTHON FILE STRINGS--------------------------##

imports = """
import webbrowser
from kivymd.uix.pickers import MDDatePicker
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
from kivy.lang import Builder
#<<<new_imports>>>
from plyer import filechooser
import os
import time
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.video import Video
os.environ["KIVY_VIDEO"] = "ffpyplayer"
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.app import MDApp
import base_strings
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
# Setting window size
window_size = Window.size
window_width = window_size[0]
window_height = window_size[1]
"""

main_screen = """
class Screen_<<<screen_id>>>(Screen):
    def __init__(self, **kwargs):
        super(Screen_<<<screen_id>>>, self).__init__(**kwargs)
        #<<<new_tab_bar_marking>>><<<screen_id>>>
        Screen<<<screen_id>>> = Builder.load_string(<<<screen_string>>>)
        self.add_widget(Screen<<<screen_id>>>)
        #<<<adding_new_widgets>>><<<screen_id>>>
        #<<<adding_actions_to_element>>><<<screen_id>>>
    #<<<adding_action_fun_to_element>>><<<screen_id>>>
        # -----------------------------END OF SCREEN----------------------------- #
"""
splash_screen="""
WindowManager:
    SplashScreen:
        name: "splash"
    #<<<splash_screen_class_id>>>:
        name: "#<<<splash_screen_id>>>"
        
<SplashScreen>:
    FitImage:
        source:"#<<launch_image>>"
        """
main_app_base_string = """
#<<<imports_marking>>>>
#<<launchscreen>>
#<<<new_tab_bar_marking>>>
#<<<new_screen_marking>>>

class SplashScreen(Screen):
    pass
    
class Videos(Video):
    pass
    
class ContentNavigationDrawer(MDBoxLayout):
    pass

class Shadow(RoundedRectangularElevationBehavior, MDBoxLayout):
    pass

class ClickableBoxLayout(ButtonBehavior, MDBoxLayout):
    pass


class WindowManager(ScreenManager):
    pass

class ScreenApp(MDApp):
    window_size = Window.size
    window_width = window_size[0]
    window_height = window_size[1]
    def build(self):
        self.icon = '#<<app_icon>>'
        self.window_manager=Builder.load_string(splash_screen)
        Clock.schedule_once(self.go_to_home,3)
        return self.window_manager

    def go_to_home(self, *args):
        screen_manager = ScreenManager()
        self.window_manager.current = '#<<<splash_screen_id>>>'
        #<<<calling_screens>>>
        return screen_manager

    

# run the app
ScreenApp().run()
"""
bottom_modal_string = """
<ItemForCustomBottomSheet@OneLineIconListItem>
    on_press: app.custom_sheet.dismiss()
    icon: ""

    IconLeftWidget:
        icon: root.icon
<ContentCustomSheet@MDBoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "10dp"
    md_bg_color:0,0,0,0
    MDBoxLayout:
        orientation:"vertical"
        height:dp(<<<height>>>+<<<border_size>>>)
        md_bg_color:rbga('<<<border_color>>>')      #card background bordercolor
        radius: [<<<border_radius>>>]
        padding:dp(5),dp(5),dp(5),dp(5)
        size_hint_y:None
        MDBoxLayout:
            height:dp(<<<height>>>)
            radius: [<<<border_radius>>>]
            padding:dp(<<<margin_left>>>), dp(<<<margin_top>>>), dp(<<<margin_right>>>), dp(<<<margin_bottom>>>)
            MDCard:
                padding:dp(<<<padding_left>>>), dp(<<<padding_top>>>), dp(<<<padding_right>>>), dp(<<<padding_bottom>>>)
                md_bg_color: rgba('<<<bg_color>>>')                                          #background color
                radius:[<<<border_radius>>>]
                height:dp(<<<height>>>)  #height
                ScrollView:
                    orientation:"vertical"
                    size_hint_y:None
                    height:dp(<<<height>>>)  ####height is adjustable for bottomsheet
                    do_scroll_x:False
                    do_scroll_y:False
"""

modal_string = """
ModalView:
    size_hint:(None, None)
    size:(100, 100)
"""
time_picker_python_string = """
        # Time picker
        def show_time<<<element_id>>>(self, *kwargs):
            picker = MDTimePicker()
            picker.bind(time=get_time<<<element_id>>>)
            picker.open()

        def get_time<<<element_id>>>(self, value):
            <<<time_picker>>>.ids.time_picker_label.text = str(value)
"""
date_picker_python_string = """
        # Date picker
        def show_date<<<element_id>>>(self, *kwargs):
            picker = MDDatePicker()
            picker.bind(on_save=on_date_save<<<element_id>>>)
            picker.open()

        def on_date_save<<<element_id>>>(self, value, instance):
            <<<date_picker>>>.ids.date_picker_label.text = str(value)
"""
image_picker_python_string="""
        def file_select<<<element_id>>>(self,*args):
            file_name = filechooser.open_file(filters=[("*.jpg"),("*.png"),("*.jpeg")])
            print(file_name)

"""
audio_player_python_string = """
        # AUDIO PLAYER
        # load audio
        audio_dir = "audio"
        audio_files = os.listdir(audio_dir)
        audio_list = [x for x in audio_files if x.endswith('mp3')]
        audio_title = "<<<audio_file_name>>>"
        if audio_title in audio_list:
            audio = SoundLoader.load('{}/{}'.format(audio_dir, audio_title))
        # ---------------------------------------------------------------#

        def volume(instance, value):
            audio.volume = value
            if audio.volume == 0:
                <<<player>>>.ids.volume_id.icon = "volume-off"
            else:
                <<<player>>>.ids.volume_id.icon = "volume-high"

            instance.bind()

        <<<player>>>.ids.volume_slider_id.bind(value=volume)

        def volume_icon(widget):
            if <<<player>>>.ids.volume_id.icon == "volume-off":
                <<<player>>>.ids.volume_id.icon = "volume-high"
                audio.volume = <<<player>>>.ids.volume_slider_id.value
            else:
                <<<player>>>.ids.volume_id.icon = "volume-off"
                audio.volume = 0

        <<<player>>>.ids.volume_id.bind(on_press=volume_icon)

        def update_progressbar(widget):
            if <<<player>>>.ids.progressbar.value < 100:
                <<<player>>>.ids.progressbar.value += 1

        def set_time(widget):
            current_time = time.strftime('%M:%S', time.gmtime(<<<player>>>.ids.progressbar.value))
            total_time = time.strftime('%M:%S', time.gmtime(audio.length))
            <<<player>>>.ids.current_time.text = " " + current_time + " / " + total_time

        def download(widget):
            pass

        def play_audio(widget):
            if audio.state == "stop":
                audio.play()
                <<<player>>>.ids.play_id.icon = "pause"
                <<<player>>>.progressbarEvent = Clock.schedule_interval(update_progressbar, audio.length / 60)
                <<<player>>>.settimeEvent = Clock.schedule_interval(set_time, 1)

            else:
                audio.stop()
                <<<player>>>.ids.play_id.icon = "play"
                <<<player>>>.progressbarEvent.cancel()
                <<<player>>>.settimeEvent.cancel()
                <<<player>>>.ids.progressbar.value = 0
                <<<player>>>.ids.current_time.text = " 00:00 / 00:00"

        <<<player>>>.ids.play_id.bind(on_press=play_audio)
        <<<player>>>.ids.download_id.bind(on_press=download)
"""

tab_bar_action_function = """
    def switch_screen_<<<tab_id>>>(self, widget):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "<<<action_screen_name>>>"
    #<<<adding_action_fun_to_element>>><<<screen_id>>>

"""
side_menu_tab_function="""
        def switch_screen_<<<side_menu_id>>>(widget):
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = "<<<action_screen_name>>>"
        #<<<adding_action_fun_to_element>>><<<elm_id>>>
"""

video_picker_python_string = """
        def file_select<<<element_id>>>(self,*args):
            file_name = filechooser.open_file(filters=[("*.mp4")])
            print(file_name)
"""
audio_picker_python_string = """
        def file_select<<<element_id>>>(self,*args):
            file_name = filechooser.open_file(filters=[("*.mp3")])
            print(file_name)
"""
video_player_python_string = """
        video_dir = "videos"
        video_files = os.listdir(video_dir)
        video_list = [x for x in video_files if x.endswith('mp4')]
        video_title = "<<<video_file_name>>>"
        if video_title in video_list:
            video = SoundLoader.load('{}/{}'.format(video_dir, video_title))
        # ---------------------------------------------------------------#

        video_player=<<<player>>>.ids.video

        def volume(instance, value):
            video_player.volume = value
            if video.volume == 0:
                <<<player>>>.ids.volume_id.icon = "volume-off"
            else:
                <<<player>>>.ids.volume_id.icon = "volume-high"

            instance.bind()
        <<<player>>>.ids.volume_slider_id.bind(value=volume)

        def update_progressbar(widget):
            if <<<player>>>.ids.progressbar.value < 100:
                <<<player>>>.ids.progressbar.value += 1

        def set_time(self):
            current_time = time.strftime('%M:%S', time.gmtime(<<<player>>>.ids.progressbar.value))
            total_time = time.strftime('%M:%S', time.gmtime(video.length))
            <<<player>>>.ids.current_time.text = " " + current_time + " / " + total_time

        def volume_icon(widget):
            if <<<player>>>.ids.volume_id.icon == "volume-off":
                <<<player>>>.ids.volume_id.icon = "volume-high"
                video_player.volume = <<<player>>>.ids.volume_slider_id.value
            else:
                <<<player>>>.ids.volume_id.icon = "volume-off"
                video_player.volume = 0

        <<<player>>>.ids.volume_id.bind(on_press=volume_icon)
        def play_audio(widget):
            if widget.icon =='play':
                widget.icon ='pause'
                <<<player>>>.ids.video.state='play'
                <<<player>>>.progressbarEvent = Clock.schedule_interval(update_progressbar, video.length / 60)
                <<<player>>>.settimeEvent = Clock.schedule_interval(set_time, 1)
            else:
                widget.icon ='play'
                <<<player>>>.ids.video.state='pause'
                <<<player>>>.progressbarEvent.cancel()
                <<<player>>>.settimeEvent.cancel()
                <<<player>>>.ids.progressbar.value = 0
                <<<player>>>.ids.current_time.text = " 00:00 / 00:00"
            return (widget.icon)

        <<<player>>>.ids.play_id.bind(on_press=play_audio)
"""
side_menu_python_string = """
        active_color = '<<<active_text_color>>>'
        inactive_color = '<<<inactive_text_color>>>'
        active_bg_color = '<<<active_tab_color>>>'
        inactive_bg_color = '<<<inactive_tab_color>>>'

        def set_tab_color(widget):
            if widget == <<<side_menu>>>.ids.<<<tab_bar_id>>>:
                <<<side_menu>>>.ids.tab1.color = active_color
                <<<side_menu>>>.ids.tab2.color = inactive_color
                <<<side_menu>>>.ids.tab3.color = inactive_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = active_bg_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = inactive_bg_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = inactive_bg_color
            elif widget == <<<side_menu>>>.ids.<<<tab_bar_id>>>:
                <<<side_menu>>>.ids.<<<tab_id>>>.color = active_color
                <<<side_menu>>>.ids.<<<tab_id>>>.color = inactive_color
                <<<side_menu>>>.ids.<<<tab_id>>>.color = inactive_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = inactive_bg_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = active_bg_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = inactive_bg_color

            elif widget == <<<side_menu>>>.ids.<<<tab_bar_id>>>:
                <<<side_menu>>>.ids.tab3.color = active_color
                <<<side_menu>>>.ids.tab1.color = inactive_color
                <<<side_menu>>>.ids.tab2.color = inactive_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = inactive_bg_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = inactive_bg_color
                <<<side_menu>>>.ids.<<<tab_bar_id>>>.md_bg_color = active_bg_color

        <<<side_menu>>>.ids.<<<tab_bar_id>>>.bind(on_press=set_tab_color)
        <<<side_menu>>>.ids.<<<tab_bar_id>>>.bind(on_press=set_tab_color)
        <<<side_menu>>>.ids.<<<tab_bar_id>>>.bind(on_press=set_tab_color)

"""

# ui_elements_action_functions
action_to_web = """
    def open_web<<<elm_id>>>(self,widget):
        webbrowser.open('<<<url>>>')
    #<<<adding_action_fun_to_element>>><<<screen_id>>>
"""
action_to_modal = """
    def open_modal<<<elm_id>>>(self, widget):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
        self.custom_sheet.open()
        #<<<adding_action_fun_to_element>>><<<screen_id>>>
        #view = Builder.load_string('modal_string')
        #view.open()
"""
action_to_screen = """
    def switch_screen<<<screen_id>>>_<<<elm_id>>><<<list_count>>>(self, widget):
        self.manager.transition = SlideTransition(direction="<<<transition>>>")
        self.manager.current = "<<<action_screen_name>>>"
    #<<<adding_action_fun_to_element>>><<<screen_id>>>
"""
app_bar_action_to_screen = """
        def switch_screen<<<screen_id>>>_<<<elm_id>>><<<list_count>>>(widget):
            self.manager.transition = SlideTransition(direction="<<<transition>>>")
            self.manager.current = "<<<action_screen_name>>>"
        #<<<adding_action_fun_to_element>>><<<screen_id>>>
"""

list_action_to_web = """
    def open_web<<<list_count>>>_<<<elm_id>>>(self,widget):
        webbrowser.open('<<<url>>>')
    #<<<adding_action_fun_to_element>>><<<screen_id>>>
"""

