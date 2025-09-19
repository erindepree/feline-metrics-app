import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "FelineMetrics | Vets",
    page_icon = ":material/stethoscope:"
)

st.title(":material/stethoscope: Vet Info")


df = pd.read_csv('./data/vets.csv')

df = df.sort_values(by='vet_id')

st.dataframe(df)