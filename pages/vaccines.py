import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "FelineMetrics | Vaccines",
    page_icon = ":material/vaccines:"
)

st.title(":material/vaccines: Mel's Vaccines")

st.write("List all vaccines with dates")

df = pd.read_csv('./data/mel/vaccines.csv', parse_dates=['date'])

st.dataframe(df)