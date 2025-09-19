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

blood_dict = pd.read_csv("./data/bloodwork_dict.csv")

plot_opts = df_blood.drop(columns=['date', 'comments', 'blood_parasites', 'rbc_morph', 'platelet_est']).columns


var_plot = st.selectbox('Select Variable to Plot:', options = plot_opts, index= 10)

fig = px.scatter(df_blood, x='date', y=var_plot, title="Bloodwork")
fig.add_shape(
    type='line',
    line_color='magenta',
    line_width=3, 
    x0=0, 
    x1 = 1, xref='paper',
    y0= blood_dict[blood_dict['test'] == var_plot]['min'],
    y1= blood_dict[blood_dict['test'] == var_plot]['min'],
    ref = 'y'
)

fig.add_shape(
    type='line',
    line_color='magenta',
    line_width=3, 
    x0=0, 
    x1 = 1, xref='paper',
    y0= blood_dict[blood_dict['test'] == var_plot]['max'],
    y1= blood_dict[blood_dict['test'] == var_plot]['max'],
    ref = 'y'
)


st.plotly_chart(fig)