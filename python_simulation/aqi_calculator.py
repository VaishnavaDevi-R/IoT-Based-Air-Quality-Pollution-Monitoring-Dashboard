def classify_aqi(aqi):
    """
    Classify AQI levels.
    """

    if aqi <= 50:
        return "Good 🟢"

    elif aqi <= 100:
        return "Moderate 🟡"

    elif aqi <= 200:
        return "Poor 🔴"

    else:
        return "Hazardous ⚫"