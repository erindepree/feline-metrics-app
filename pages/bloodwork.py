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
df_blood.sort_values(by='date')

plot_opts = df_blood.drop(columns=['date', 'comments', 'blood_parasites', 'rbc_morph', 'platelet_est']).columns


var_plot = st.radio('Select Variable to Plot:', options = plot_opts, index= 10)

fig = px.scatter(df_blood, x='date', y=var_plot, title="Bloodwork")

st.plotly_chart(fig)