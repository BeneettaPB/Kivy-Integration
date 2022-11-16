screen_1783_string = """ 
AnchorLayout:
    # apply padding top which is equal to height of tab bar
    padding:[dp(0), dp(0), dp(0), dp(0)]
    # padding top will be 0 if no tab bar      #screen padding
    anchor_x:'left'                  #screen horizontal alignment
    anchor_y:'top'                    #screen vertical alignment
    canvas:
        Color:
            rgba:(1.0, 1.0, 1.0, 1.0)                         #screen background color
        Rectangle:
            pos:self.pos
            size:(app.window_width, app.window_height-0-0)  # (800,600) without tabbar
                         #screen background image
    MDBoxLayout:
        id:id_1783
        orientation:'vertical'
        adaptive_height: True
        adaptive_width: True   
"""
check_box__string = """
#:import utils kivy.utils 
MDBoxLayout:
    padding:[dp(0), dp(0), dp(0), dp(0)]                              
    size_hint:(None, None)
    size: dp(200),dp(50)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        id:box_padding
        padding:[dp(0), dp(0), dp(0), dp(0)]                                              #padding
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
                selected_color:rgba('#ffffff') # active color
                unselected_color:rgba('#9D96A5FF') # inactive color
                active:True
                # checkbox_icon_down:'circle-slice-8'
                allow_no_selection:False
                size_hint:(None,None)
                size:(dp(50),dp(50))
            Label:
                text:'Checkbox'  # button
                font_size:'15px'  # font size
                font_name:'fonts/open-sans.regular.ttf'  # font type
                color:rgba('#eb4034')  # font color
                size_hint:(None,None)
                size:(dp(150),dp(50))
                text_size:self.size
                halign:"left"  # text alignment
                valign:'center'
"""
check_box__string = """
#:import utils kivy.utils 
MDBoxLayout:
    padding:[dp(0), dp(0), dp(0), dp(0)]                              
    size_hint:(None, None)
    size: dp(200),dp(50)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        id:box_padding
        padding:[dp(0), dp(0), dp(0), dp(0)]                                              #padding
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
                selected_color:rgba('#ffffff') # active color
                unselected_color:rgba('#9D96A5FF') # inactive color
                active:True
                # checkbox_icon_down:'circle-slice-8'
                allow_no_selection:False
                size_hint:(None,None)
                size:(dp(50),dp(50))
            Label:
                text:'Checkbox'  # button
                font_size:'15px'  # font size
                # font_name:'fonts/open-sans.regular.ttf'  # font type
                color:rgba('#eb4034')  # font color
                size_hint:(None,None)
                size:(dp(150),dp(50))
                text_size:self.size
                halign:"left"  # text alignment
                valign:'center'
"""
rating_bar_19_string = """
#:import utils kivy.utils 
# for margin
MDBoxLayout:
    #: set ratingbar_icon 'star-outline'
    #: set icon_color_inactive [.1,1,1,1]
    #: set icon_color_active [1,0,0,1]
    
    id:box_padding
    # md_bg_color:[1, .1, 1, .1]
    padding:[dp(10), dp(10), dp(10), dp(10)]                              
    size_hint:(None, None)
    size: dp(104),dp(70)                                               #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    AnchorLayout:
        id:anchor_padding    
        padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
        size_hint:(None, None)
        size:(dp(250), dp(50))  # width, height
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
radio_button_10_string = """
#:import utils kivy.utils 
MDBoxLayout:
    padding:[dp(0), dp(0), dp(0), dp(0)]  # margin
    size_hint:(None, None)
    size:(dp(200), dp(100))  # margin + box_padding size
    adaptive_height:True
    adaptive_width:True
    MDBoxLayout:
        id:box_padding
        padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
        size_hint:(None, None)
        size:(dp(84), dp(34))  # width, height
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
radio_button_10_string = """
#:import utils kivy.utils 
MDBoxLayout:
    padding:[dp(0), dp(0), dp(0), dp(0)]  # margin
    size_hint:(None, None)
    size:(dp(200), dp(100))  # margin + box_padding size
    adaptive_height:True
    adaptive_width:True
    MDBoxLayout:
        id:box_padding
        padding:[dp(0), dp(0), dp(0), dp(0)]  # padding
        size_hint:(None, None)
        size:(dp(84), dp(34))  # width, height
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
text_field__string = """
#:import utils kivy.utils
#:import hex kivy.utils.get_color_from_hex 
MDBoxLayout:
    id:box1
    padding:[dp(0), dp(0), dp(0), dp(0)]                              
    size_hint:None,None
    size: dp(150),dp(50)                     #width, height
    pos_hint: {'center_x': .5, 'center_y': .5}
    Shadow:
        pos_hint: {'center_x': .5, 'center_y': .5}
        adaptive_height:True
        adaptive_width:True
        shadow_pos: dp(0) + dp(0), dp(-0) + dp(0)   # (shadow size , shadow pos(0-20)) 
        elevation: 0 #blur
        soft_shadow_cl:rgba('#000000')
        radius:[dp(0)]  
        MDCard:
            id:card1
            padding:[5]                                                         #border size
            md_bg_color: rgba("#3cdec8")                    #border color
            radius:[5]                                                         #border radius 1
            size_hint:None,None
            size:(dp(150), dp(50))                                             #width, height2 #adjust box1 size
            MDCard:
                id:card2
                padding:[dp(0), dp(0), dp(0), dp(0)]
                # md_bg_color: rgba("#e8e582")                                        #bg color
                radius:[5]                                                     #border radius 2
                pos_hint: {'x':0, 'top':1}
                MDTextField:
                    id:action_id_
                    text:''
                    font_size: '15'                       #font size
                    # font_name: 'fonts/open-sans.regular.ttf'    #font type
                    text_color: rgba("#FFFFFF")                     #text color
                    halign:"center"                           #text alignment
                    input_type:"text"
                    current_hint_text_color:rgba("")   # Hint text color
                    # input_filter:'int'
                    size_hint:(None,None)
                    size:(dp(150), dp(50))             #width
                    valign:'center'
"""
text_8831_string = """
#:import utils kivy.utils
#:import hex kivy.utils.get_color_from_hex 
MDBoxLayout:
    padding:[dp(0), dp(0), dp(0), dp(0)]                              
    pos_hint: {'center_x': .5, 'center_y': .5}
    size_hint:(None, None)
    size: dp(100),dp(100)                                               #width, height
    ClickableBoxLayout:
        id:action_id_8831
        padding:[dp(0), dp(0), dp(0), dp(0)]
        size_hint:(None, None)
        size:(dp(100), dp(100))  # width, height
        md_bg_color:rgba("#F4FF86")
        orientation:'vertical'

        MDLabel:
            text: 'textjfh'                           #text
            bold: True
            font_size: '15'                       #font size
            # font_name: 'fonts/great-vibes.regular.ttf'    #font type
            color: rgba("#F21F1F")                     #text color
            halign:"left"                           #text alignment
            #md_bg_color: rgba("#cf8f522")                                        #bg color
"""