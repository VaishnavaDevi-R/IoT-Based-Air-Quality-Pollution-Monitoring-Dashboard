import pandas as pd

df = pd.read_csv("data/air_quality_logs.csv")

avg_aqi = round(df["AQI"].mean(), 2)
max_aqi = df["AQI"].max()
min_aqi = df["AQI"].min()

avg_temp = round(df["Temperature"].mean(), 2)
avg_humidity = round(df["Humidity"].mean(), 2)

report = f"""
=================================
AIR QUALITY REPORT
=================================

Total Records: {len(df)}

AQI Statistics
--------------
Average AQI: {avg_aqi}
Maximum AQI: {max_aqi}
Minimum AQI: {min_aqi}

Temperature Statistics
----------------------
Average Temperature: {avg_temp} °C

Humidity Statistics
-------------------
Average Humidity: {avg_humidity} %

=================================
"""

with open(
    "outputs/reports/daily_air_quality_report.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(report)

print("✅ Report Generated")

summary = pd.DataFrame({
    "Metric": [
        "Average AQI",
        "Maximum AQI",
        "Minimum AQI",
        "Average Temperature",
        "Average Humidity"
    ],
    "Value": [
        avg_aqi,
        max_aqi,
        min_aqi,
        avg_temp,
        avg_humidity
    ]
})

summary.to_csv(
    "outputs/reports/summary_statistics.csv",
    index=False
)

print("✅ Summary Statistics CSV Generated")