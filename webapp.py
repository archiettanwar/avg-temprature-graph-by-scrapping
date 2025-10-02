import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("time_temp.txt")

st.title("Avg_temperatures")

figure=px.line(x=df["date"],y=df['temp'],
               labels={"x":"dates","y":"avg_temperatures"})

st.plotly_chart(figure)
