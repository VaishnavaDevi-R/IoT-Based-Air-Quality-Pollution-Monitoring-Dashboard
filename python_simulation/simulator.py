import random
from datetime import datetime

from aqi_calculator import classify_aqi
from alerts import check_alert
from logger import save_log


current_pm25 = 35
current_pm10 = 60
current_co2 = 550
current_temp = 29
current_humidity = 65

def generate_sensor_data():

    global current_pm25
    global current_pm10
    global current_co2
    global current_temp
    global current_humidity

    current_pm25 += random.randint(-5, 5)
    current_pm10 += random.randint(-8, 8)
    current_co2 += random.randint(-20, 20)

    current_temp += random.uniform(-0.4, 0.4)
    current_humidity += random.uniform(-1.2, 1.2)

    current_pm25 = max(5, min(current_pm25, 250))
    current_pm10 = max(10, min(current_pm10, 350))
    current_co2 = max(350, min(current_co2, 2000))

    current_temp = max(20, min(current_temp, 45))
    current_humidity = max(30, min(current_humidity, 90))

    aqi = int(
        (current_pm25 * 0.5) +
        (current_pm10 * 0.3) +
        ((current_co2 / 10) * 0.2)
    )

    return (
        aqi,
        current_pm25,
        current_pm10,
        current_co2,
        round(current_temp, 1),
        round(current_humidity, 1)
    )

def main():

    print("\nIoT Air Quality Monitoring Started...\n")

    for _ in range(50):

        aqi, pm25, pm10, co2, temperature, humidity = generate_sensor_data()

        status = classify_aqi(aqi)

        alert = check_alert(aqi)

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        save_log([
            timestamp,
            aqi,
            pm25,
            pm10,
            co2,
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