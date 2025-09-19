import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "FelineMetrics | Clinics",
    page_icon = ":material/local_hospital:"
)

st.title(":material/local_hospital: Vet Info")


df = pd.read_csv('./data/clinics.csv')

df = df.sort_values(by='clinic_id')

st.dataframe(df)