import paho.mqtt.client as mqtt
import random
import time

# Configuration du broker MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "iot/capteur/dht"

# Fonction pour simuler les données du capteur DHT
def simulate_dht():
    temperature = round(random.uniform(20.0, 30.0), 2)  # Température entre 20.0 et 30.0
    humidity = round(random.uniform(30.0, 60.0), 2)  # Humidité entre 30.0 et 60.0
    return {"temperature": temperature, "humidity": humidity}

# Callback pour la connexion au broker MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT")
    else:
        print(f"Échec de la connexion, code de retour {rc}")

# Création du client MQTT
client = mqtt.Client()
client.on_connect = on_connect

try:
    # Connexion au broker MQTT
    client.connect(BROKER, PORT, 60)
    client.loop_start()  # Démarre la boucle de gestion des messages

    while True:
        data = simulate_dht()
        client.publish(TOPIC, str(data))
        print(f"Données publiées : {data}")
        time.sleep(5)

except KeyboardInterrupt:
    print("Arrêt du script...")
    client.loop_stop()  # Arrête la boucle de gestion des messages
    client.disconnect()  # Déconnexion du broker MQTT
    print("Déconnecté du broker MQTT")