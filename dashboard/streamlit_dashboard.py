import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime

from streamlit_autorefresh import st_autorefresh

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Auto Refresh Every 5 Seconds
st_autorefresh(
    interval=5000,
    key="air_quality_refresh"
)

# -------------------------
# Title
# -------------------------
st.title("🌍 IoT Air Quality & Pollution Monitoring Dashboard")

st.write(
    "Last Refresh:",
    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

# -------------------------
# Load Data
# -------------------------
try:

    df = pd.read_csv("data/air_quality_logs.csv")

    if df.empty:
        st.warning("No sensor data available.")
        st.stop()

    latest = df.iloc[-1]

    # -------------------------
    # KPI Cards
    # -------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "AQI",
            latest["AQI"]
        )

    with col2:
        st.metric(
            "Temperature (°C)",
            latest["Temperature"]
        )

    with col3:
        st.metric(
            "Humidity (%)",
            latest["Humidity"]
        )

    with col4:
        st.metric(
            "Status",
            latest["Status"]
        )

    st.divider()

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=float(latest["AQI"]),
            title={"text": "Air Quality Index"},
            gauge={
                "axis": {"range": [0, 350]},
                "steps": [
                    {"range": [0, 50]},
                    {"range": [50, 100]},
                    {"range": [100, 200]},
                    {"range": [200, 350]}
                ]
            }
        )
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    # -------------------------
    # AQI Status Indicator
    # -------------------------
    status = str(latest["Status"])

    if "Good" in status:
        st.success(
            f"🟢 Air Quality Status: {status}"
        )

    elif "Moderate" in status:
        st.warning(
            f"🟡 Air Quality Status: {status}"
        )

    elif "Poor" in status:
        st.error(
            f"🔴 Air Quality Status: {status}"
        )

    else:
        st.error(
            f"⚫ Air Quality Status: {status}"
        )

    # -------------------------
    # Alert Section
    # -------------------------
    alert = str(latest["Alert"])

    if "CRITICAL" in alert:
        st.error(alert)

    elif "WARNING" in alert:
        st.warning(alert)

    else:
        st.success(alert)

    st.divider()

    # -------------------------
    # Latest Reading
    # -------------------------
    st.subheader("📡 Latest Sensor Reading")

    colA, colB, colC, colD = st.columns(4)

    with colA:
        st.info(f"🕒 {latest['Timestamp']}")

    with colB:
        st.info(f"🌫 AQI : {latest['AQI']}")

    with colC:
        st.info(f"🌡 Temp : {latest['Temperature']} °C")

    with colD:
        st.info(f"💧 Humidity : {latest['Humidity']} %")

    st.divider()

    # -------------------------
    # Recent Data Only
    # -------------------------
    recent_df = df.tail(100)

    # -------------------------
    # AQI Trend
    # -------------------------
    fig_aqi = px.line(
        recent_df,
        x="Timestamp",
        y="AQI",
        title="AQI Trend (Latest 100 Readings)"
    )

    st.plotly_chart(
        fig_aqi,
        use_container_width=True
    )

    fig_hist = px.histogram(
        df,
        x="AQI",
        nbins=20,
        title="AQI Distribution"
    )

    st.plotly_chart(
        fig_hist,
        use_container_width=True
    )

    # -------------------------
    # Temperature Trend
    # -------------------------
    fig_temp = px.line(
        recent_df,
        x="Timestamp",
        y="Temperature",
        title="Temperature Trend"
    )

    st.plotly_chart(
        fig_temp,
        use_container_width=True
    )

    # -------------------------
    # Humidity Trend
    # -------------------------
    fig_humidity = px.line(
        recent_df,
        x="Timestamp",
        y="Humidity",
        title="Humidity Trend"
    )

    st.plotly_chart(
        fig_humidity,
        use_container_width=True
    )

    # -------------------------
    # Historical Data
    # -------------------------
    st.subheader("📋 Historical Data")

    st.dataframe(
        recent_df.tail(20),
        use_container_width=True
    )

    st.subheader("📊 Summary Statistics")

    st.dataframe(
        df[["AQI", "Temperature", "Humidity"]]
        .describe(),
        use_container_width=True
    )

    # -------------------------
    # Download CSV
    # -------------------------
    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇ Download CSV Report",
        data=csv,
        file_name="air_quality_report.csv",
        mime="text/csv"
    )

    # -------------------------
    # Footer
    # -------------------------
    st.markdown("---")

    st.caption(
        "🌍 IoT Air Quality & Pollution Monitoring Dashboard | "
        "Python Simulation + Streamlit + Data Analytics"
    )

except Exception as e:

    st.error(
        f"Error Loading Data: {e}"
    )