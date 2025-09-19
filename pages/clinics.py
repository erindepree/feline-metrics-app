import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "FelineMetrics | Clinics",
    page_icon = ":material/local_hospital:"
)

st.title(":material/local_hospital: Clinic Info")


df = pd.read_csv('./data/clinics.csv')

st.dataframe(df)