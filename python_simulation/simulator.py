import random
from datetime import datetime

from aqi_calculator import classify_aqi
from alerts import check_alert
from logger import save_log


def generate_sensor_data():

    aqi = random.randint(20, 350)

    temperature = round(
        random.uniform(20, 40), 1
    )

    humidity = round(
        random.uniform(30, 90), 1
    )

    return aqi, temperature, humidity


def main():

    print("\nIoT Air Quality Monitoring Started...\n")

    for _ in range(50):

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

        print("=" * 50)
        print(f"Timestamp   : {timestamp}")
        print(f"AQI         : {aqi}")
        print(f"Temperature : {temperature}°C")
        print(f"Humidity    : {humidity}%")
        print(f"Status      : {status}")
        print(f"Alert       : {alert}")
        print("=" * 50)


if __name__ == "__main__":
    main()