import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

state = {"sensor1": False, "sensor2": False, "door_open": False, "light_on": False}

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
 
    if msg.topic == "sensor1":
        state["sensor1"] = payload == "true"
    elif msg.topic == "sensor2":
        state["sensor2"] = payload == "true"
 
    state["door_open"] = state["sensor1"]

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883)
client.subscribe("sensor1")
client.subscribe("sensor2")
client.loop_start()
