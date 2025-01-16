import time
import paho.mqtt.client as mqtt
import random

# Configuration du broker MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "sensors/dht"

# Simulation du capteur DHT
def simulate_sensor():
    while True:
        # Générer des valeurs aléatoires pour la température et l'humidité
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)

        # Créer un message JSON
        payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'

        # Publier les données sur le broker MQTT
        client.publish(TOPIC, payload)
        print(f"Données envoyées : {payload}")
        time.sleep(2)  # Pause de 5 secondes

# Configuration du client MQTT
client = mqtt.Client()
client.connect(BROKER, PORT)

# Lancer la simulation
simulate_sensor()