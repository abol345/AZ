from kivymd.uix.screen import MDScreen
from mqtt_client import set_dashboard


class DashboardScreen(MDScreen):

    def on_enter(self):
        set_dashboard(self)

    def update_value(self, topic, value):

        if topic == "AZ/Voltage":
            self.ids.voltage.text = value + " V"

        elif topic == "AZ/Current":
            self.ids.current.text = value + " A"


        elif topic == "AZ/Temperature":
            self.ids.temp.text = value + " °C"

        elif topic == "AZ/Menu":
            self.ids.menu.text = value

        elif topic == "AZ/Error":
            self.ids.status.text = value

        elif topic == "AZ/Fail":
            self.ids.fail.text = value
