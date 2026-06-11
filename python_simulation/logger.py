import csv
import os

FILE_NAME = "data/air_quality_logs.csv"


def save_log(row):

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "AQI",
                "Temperature",
                "Humidity",
                "Status",
                "Alert"
            ])

        writer.writerow(row)