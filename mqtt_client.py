import paho.mqtt.client as mqtt
from kivy.clock import Clock

BROKER = "broker.hivemq.com"
PORT = 1883

client = mqtt.Client()

def connect():
    client.connect(BROKER, PORT, 60)
    client.subscribe("AZ/Voltage")
    client.subscribe("AZ/Current")
    client.subscribe("AZ/Temperature")
    client.subscribe("AZ/Menu")
    client.subscribe("AZ/Error")
    client.subscribe("AZ/Fail")
    client.loop_start()
def on_connect(client, userdata, flags, rc):
    print("Connected =", rc)



def send_test():

    client.publish("AZ/Test", "Hello ESP32")
def send_command(cmd):
    client.publish("AZ/CMD", cmd)
    print("MQTT Send:", cmd)

control = None
dashboard = None

def set_dashboard(scr):
    global dashboard
    dashboard = scr
def set_control(scr):
    global control
    control = scr
def on_message(client, userdata, msg):

    topic = msg.topic
    value = msg.payload.decode()

    print(topic, value)

    if topic == "AZ/Menu":

        if control:
            Clock.schedule_once(
                lambda dt: control.update_menu(value)
            )

    else:

        if dashboard:
            Clock.schedule_once(
                lambda dt: dashboard.update_value(topic, value)
            )
client.on_message = on_message      
client.on_connect = on_connect
