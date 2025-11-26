import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import os

st.set_page_config(page_title="Attendance Dashboard", layout="wide")

st.title("Attendance Monitoring System")
st.markdown("Live attendance records updated every few seconds.")

# Sidebar control for refresh interval
refresh_interval = st.sidebar.slider("Refresh interval (seconds)", 1, 10, 2)

# Auto-refresh every refresh_interval seconds
count = st_autorefresh(interval=refresh_interval * 1000, limit=None, key="refresh")

date = datetime.now().strftime("%d-%m-%Y")
attendance_file = f"Attendance/Attendance_{date}.csv"

if os.path.isfile(attendance_file):
    df = pd.read_csv(attendance_file)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    st.warning(f"No attendance file found for {date} yet.")

st.markdown(f"Last updated at: {datetime.now().strftime('%H:%M:%S')}")
