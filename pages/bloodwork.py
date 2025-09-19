import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "FelineMetrics | Bloodwork",
    page_icon = ":material/health_metrics:"
)

st.title(":material/health_metrics: Mel's Bloodwork")

st.write("Bloodwork graphs here")

df_blood = pd.read_csv("./data/mel/bloodwork.csv")

st.dataframe(df_blood)