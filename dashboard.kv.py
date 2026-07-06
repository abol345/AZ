
    

  
    <DashboardScreen>:
    md_bg_color:"#101418"

    MDBoxLayout:

        orientation:"vertical"

        spacing:"15dp"

        padding:"15dp"

        MDTopAppBar:

            title:"A.Z Smart Power"

            elevation:4

        ScrollView:

            MDBoxLayout:

                orientation:"vertical"

                adaptive_height:True

                spacing:"15dp"

                MDCard:

                    radius:[20]

                    size_hint_y:None

                    height:"90dp"

                    md_bg_color:"#1E2A32"

                    MDBoxLayout:

                        padding:"15dp"

                        MDLabel:

                            text:"⚡ Voltage"

                            font_style:"H6"

                        MDLabel:

                            id:voltage

                            text:"220.0 V"

                            halign:"right"

                MDCard:

                    radius:[20]

                    size_hint_y:None

                    height:"90dp"

                    md_bg_color:"#1E2A32"

                    MDBoxLayout:

                        padding:"15dp"

                        MDLabel:

                            text:"🔌 Current"

                            font_style:"H6"

                        MDLabel:

                            id:current

                            text:"0.00 A"

                            halign:"right"

                MDCard:

                    radius:[20]

                    size_hint_y:None

                    height:"90dp"

                    md_bg_color:"#1E2A32"

                    MDBoxLayout:

                        padding:"15dp"

                        MDLabel:

                            text:"💡 Power"

                            font_style:"H6"

                        MDLabel:

                            id:power

                            text:"0 W"

                            halign:"right"

                MDCard:

                    radius:[20]

                    size_hint_y:None

                    height:"90dp"

                    md_bg_color:"#1E2A32"

                    MDBoxLayout:

                        padding:"15dp"

                        MDLabel:

                            text:"🔋 Energy"

                            font_style:"H6"

                        MDLabel:

                            id:energy

                            text:"0.000 kWh"

                            halign:"right"

                MDCard:

                    radius:[20]

                    size_hint_y:None

                    height:"90dp"

                    md_bg_color:"#1E2A32"

                    MDBoxLayout:

                        padding:"15dp"

                        MDLabel:

                            text:"🌡 Temperature"

                            font_style:"H6"

                        MDLabel:

                            id:temp

                            text:"25 °C"

                            halign:"right"

                MDCard:

                    radius:[20]

                    size_hint_y:None

                    height:"90dp"

                    md_bg_color:"#1E2A32"

                    MDBoxLayout:

                        padding:"15dp"

                        MDLabel:

                            text:"⚠ Status"

                            font_style:"H6"

                        MDLabel:

                            id:status

                            text:"No Error"

                            halign:"right"

                MDCard:

                    radius:[20]

                    size_hint_y:None

                    height:"250dp"

                    md_bg_color:"#1E2A32"

                    MDLabel:

                        text:"Live Graph"

                        halign:"center"
                        MDRaisedButton:
    text: "Control"

    pos_hint: {"center_x": .5}

    on_release:
        app.root.current="control"
