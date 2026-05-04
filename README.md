# IOTAssignment

## Smart Weather Station (IoT System)

My project is a personal Smart Weather Station designed to collect  data (temperature and humidity) using a DHT11 sensor connected to my Raspberry Pi. The system processes, formats, and transmits sensor data for live monitoring and visualisation.

## System Overview

The project implements a complete IoT architecture:

- **Sensor Layer:** DHT11 temperature and humidity sensor
- **Processing Layer:** Raspberry Pi running Python scripts
- **Gateway Layer:** Blynk Cloud
- **Application Layer:** Mobile dashboard and web dashboard on blynk with live graphs and gauges

## Features Implemented

- Raspberry Pi configured and accessed via SSH  
- GitHub repository created and linked to device  
- Python virtual environment set up for dependency management  
- DHT11 sensor successfully integrated with Raspberry Pi GPIO  
- Real-time sensor data collection (temperature & humidity)  
- JSON-formatted telemetry with timestamped readings  
- Live data transmission to Blynk cloud using HTTP API  
- Mobile dashboard displaying:
  - Real-time temperature gauge  
  - Real-time humidity gauge  
  - Historical data graph (time-series visualisation)

## Technologies Used

- Python  
- Raspberry Pi OS  
- DHT11 Temperature & Humidity Sensor  
- GPIO (adafruit-circuitpython-dht library)  
- Blynk IoT Cloud Platform  
- HTTP REST API  
- JSON data formatting  
- Git & GitHub  

## Data Format

Sensor readings are structured as JSON before logging and transmission:

```json
{
  "temperature": 18.3,
  "humidity": 58,
  "timestamp": 1777859514.73
}
