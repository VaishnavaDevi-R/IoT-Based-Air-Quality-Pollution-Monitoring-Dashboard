import csv
import os

FILE_NAME = "data/air_quality_logs.csv"

def save_log(row):

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow([
                "Timestamp",
                "AQI",
                "PM25",
                "PM10",
                "CO2",
                "Temperature",
                "Humidity",
                "Status",
                "Alert"
            ])

        writer.writerow(row)