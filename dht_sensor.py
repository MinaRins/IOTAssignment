import time
import adafruit_dht
import board
from blynk import Blynk

blynk = Blynk(BLYNK_AUTH)
BLYNK_AUTH = "W_oWJ1QxAj7f_u-BDfvAynUFtdlkiK5z"

dht = adafruit_dht.DHT11(board.D5)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        print(f"Temp: {temperature:.1f}°C")
        print(f"Humidity: {humidity:.1f}%")

    except RuntimeError:
        print("Read failed, retrying...")

    time.sleep(2)
import adafruit_dht
import board

dht = adafruit_dht
