import time
import requests
import adafruit_dht
import board

BLYNK_TOKEN = "W_oWJ1QxAj7f_u-BDfvAynUFtdlkiK5z"

dht = adafruit_dht.DHT11(board.D5)

def send(pin, value):
    url = f"https://blynk.cloud/external/api/update?token={BLYNK_TOKEN}&{pin}={value}"
    try:
        r = requests.get(url, timeout=5)
        print("Sent:", pin, value, "| Response:", r.status_code)
    except Exception as e:
        print("Error:", e)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        if temperature is not None and humidity is not None:
            print(f"Temp: {temperature:.1f}°C")
            print(f"Humidity: {humidity:.1f}%")

            send("v0", temperature)
            send("v1", humidity)

    except RuntimeError:
        print("Read failed, retrying...")

    time.sleep(2)
