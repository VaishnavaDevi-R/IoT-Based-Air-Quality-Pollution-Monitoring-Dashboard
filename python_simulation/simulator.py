import random
import time
from datetime import datetime

from aqi_calculator import classify_aqi
from alerts import check_alert
from logger import save_log

current_aqi = 70
current_temp = 29.0
current_humidity = 65.0

def generate_sensor_data():

    global current_aqi
    global current_temp
    global current_humidity

    current_aqi += random.randint(-5, 5)
    current_temp += random.uniform(-0.3, 0.3)
    current_humidity += random.uniform(-1.0, 1.0)

    current_aqi = max(20, min(current_aqi, 350))
    current_temp = max(20, min(current_temp, 45))
    current_humidity = max(30, min(current_humidity, 90))

    return (
        current_aqi,
        round(current_temp, 1),
        round(current_humidity, 1)
    )

while True:

    aqi, temperature, humidity = generate_sensor_data()

    status = classify_aqi(aqi)

    alert = check_alert(aqi)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    save_log([
        timestamp,
        aqi,
        temperature,
        humidity,
        status,
        alert
    ])

    print(
        f"{timestamp} | AQI={aqi} | Temp={temperature}°C | Humidity={humidity}%"
    )

    time.sleep(5)