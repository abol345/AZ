from kivymd.uix.screen import MDScreen
from mqtt_client import send_command
from mqtt_client import set_control
class ControlScreen(MDScreen):

    def on_button(self, cmd):

        print(cmd)
        send_command(cmd)

        # بعداً MQTT اینجا قرار می‌گیرد


    def on_enter(self):
        set_control(self)
    def update_menu(self, value):
        self.ids.menu.text = value
