import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "FelineMetrics | Medical Encounters",
    page_icon = ":material/medical_services:"
)

st.title(":material/medical_services: Mel's Medical Encounters")


df = pd.read_csv("./data/mel/incidents.csv", parse_dates=['date'])

df = df.sort_values(by='date')

st.dataframe(df)