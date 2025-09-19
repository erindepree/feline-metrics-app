import pandas as pd
import plotly.express as px
from datetime import date
import streamlit as st

st.set_page_config(
    page_title = "FelineMetrics | Bloodwork",
    page_icon = ":material/health_metrics:"
)

st.title(":material/health_metrics: Mel's Bloodwork")

st.write("Bloodwork graphs here")

df_blood = pd.read_csv("./data/mel/bloodwork.csv", parse_dates=['date'])

plot_opts = df_blood.drop(columns=['date', 'comments', 'blood_parasites', 'rbc_morph', 'platelet_est']).columns

# st.dataframe(df_blood)
df_blood.sort_values(by='date')

var_plot = st.radio('Select Variable to Plot:', options = plot_opts, index= 10)

fig = px.line(df_blood, x='date', y=var_plot, title="Bloodwork")

st.plotly_chart(fig)