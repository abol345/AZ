from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from mqtt_client import connect
from control import ControlScreen
from dashboard import DashboardScreen
from mqtt_client import connect, send_test
class AZApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        Builder.load_file("dashboard.kv")
        Builder.load_file("control.kv")

        sm = ScreenManager()

       

        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ControlScreen(name="control"))
        connect()
        send_test()

        return sm


AZApp().run()
