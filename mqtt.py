import paho.mqtt.client as mqtt

connected = False
host = "192.168.0.2"
port = 1883
topic = "cmnd/led_strip/power"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code " + str(rc))
        global connected
        connected = True
    else:
        print("Connection failed")


client = mqtt.Client("MQTT Python")
client.on_connect = on_connect
client.connect(host, port)

while True:
    payload = "toggle"
    client.publish(topic, payload, qos=0, retain=False)
