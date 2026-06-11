import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 IoT Air Quality & Pollution Monitoring Dashboard")

try:
    df = pd.read_csv("data/air_quality_logs.csv")

    latest = df.iloc[-1]

    aqi = latest["AQI"]
    temp = latest["Temperature"]
    humidity = latest["Humidity"]
    status = latest["Status"]
    alert = latest["Alert"]

    col1, col2, col3 = st.columns(3)

    col1.metric("AQI", latest["AQI"])
    col2.metric("PM2.5", latest["PM25"])
    col3.metric("PM10", latest["PM10"])

    col4, col5, col6 = st.columns(3)

    col4.metric("CO₂ (ppm)", latest["CO2"])
    col5.metric("Temperature", latest["Temperature"])
    col6.metric("Humidity", latest["Humidity"])

    st.markdown("---")

    if "CRITICAL" in alert:
        st.error(alert)
    elif "WARNING" in alert:
        st.warning(alert)
    else:
        st.success(alert)

    st.markdown("---")

    fig1 = px.line(
        df,
        x="Timestamp",
        y="AQI",
        title="AQI Trend"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2 = px.line(
        df,
        x="Timestamp",
        y=["Temperature", "Humidity"],
        title="Temperature & Humidity Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    fig_pm = px.line(
        df,
        x="Timestamp",
        y=["PM25", "PM10"],
        title="Particulate Matter Trends"
    )

    st.plotly_chart(
        fig_pm,
        use_container_width=True
    )

    fig_co2 = px.line(
        df,
        x="Timestamp",
        y="CO2",
        title="CO₂ Concentration Trend"
    )

    st.plotly_chart(
        fig_co2,
        use_container_width=True
    )
    
    st.markdown("### Historical Data")

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇ Download CSV Report",
        data=csv,
        file_name="air_quality_report.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(
        f"Error Loading Data: {e}"
    )