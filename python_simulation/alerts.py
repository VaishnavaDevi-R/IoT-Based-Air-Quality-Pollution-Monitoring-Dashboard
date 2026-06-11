def check_alert(aqi):

    if aqi > 200:
        return "🚨 CRITICAL ALERT"

    elif aqi > 100:
        return "⚠️ POLLUTION WARNING"

    return "Normal"