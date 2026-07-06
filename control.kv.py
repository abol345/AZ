<ControlScreen>:

    MDScreen:

        md_bg_color:"#101418"

        MDBoxLayout:

            orientation:"vertical"

            spacing:"15dp"

            padding:"15dp"

            MDTopAppBar:

                title:"Device Control"

                anchor_title:"center"

            MDCard:

                size_hint_y:None

                height:"80dp"

                MDBoxLayout:

                    padding:"15dp"

                    MDLabel:

                        text:"Menu Status"

                    MDLabel:

                        id:menu

                        text:"READY"

                        halign:"right"

            MDRaisedButton:

                text:"ON"

            MDRaisedButton:

                text:"OFF"

            MDRaisedButton:

                text:"MENU"

            MDRaisedButton:

                text:"NEXT"

            MDRaisedButton:

                text:"UP"

            MDRaisedButton:

                text:"DOWN"

            MDRaisedButton:

                text:"RESET"

            MDRaisedButton:

                text:"Dashboard"

                on_release:

                    app.root.current="dashboard"
