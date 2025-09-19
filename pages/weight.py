import streamlit as st
from datetime import date
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title= "FelineMetrics | Weight",
    page_icon= ":material/monitor_weight:"
)

st.title(":material/monitor_weight: Mel's Weight")
#st.write(
#    "Keep track of Mel's Weight"
#)

df = pd.DataFrame([
    {'pet': 'Mel', 'date': date(2013, 11, 1), 'weight': 9.0, 'location': 'park_vet', 'notes': ''},
    {'pet': 'Mel', 'date': date(2014, 11, 1), 'weight': 9.0, 'location': 'park_vet', 'notes': ''},
    {'pet': 'Mel', 'date': date(2015, 11, 1), 'weight': 9.3, 'location': 'park_vet', 'notes': ''},
    {'pet': 'Mel', 'date': date(2021, 7, 27), 'weight': 8.2, 'location': 'park_vet', 'notes': ''},
    {'pet': 'Mel', 'date': date(2022, 7, 14), 'weight': 8.2, 'location': 'park_vet', 'notes': ''},
    {'pet': 'Mel', 'date': date(2023, 3, 27), 'weight': 9.5, 'location': 'freeport', 'notes': ''},
    {'pet': 'Mel', 'date': date(2023, 4, 27), 'weight': 8.8, 'location': 'yarmouth', 'notes': ''},
    {'pet': 'Mel', 'date': date(2024, 6, 1), 'weight': 9.5, 'location': 'yarmouth', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 5, 12), 'weight': 7.5, 'location': 'yarmouth', 'notes': 'vet: good weight, stay below 8 pounds'},
    {'pet': 'Mel', 'date': date(2025, 6, 22), 'weight': 7.72, 'location': 'wecare', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 6, 30), 'weight': 7.94, 'location': 'three_notch', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 7, 14), 'weight': 7.79, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 7, 16), 'weight': 7.74, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 7, 18), 'weight': 7.68, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 7, 23), 'weight': 7.87, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 7, 28), 'weight': 7.80, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 7, 31), 'weight': 7.80, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 8, 8), 'weight': 7.89, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 8, 10), 'weight': 7.96, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 8, 16), 'weight': 7.97, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 8, 20), 'weight': 7.90, 'location': 'home', 'notes': ''},
    {'pet': 'Mel', 'date': date(2025, 9, 17), 'weight': 7.95, 'location': 'home', 'notes': ''}
])


fig = px.scatter(df, x='date', y='weight')

fig.add_shape(
    type='line',
    line_color='magenta',
    line_width=3, 
    x0=0, 
    x1 = 1, 
    xref='paper',
    y0= 8,
    y1= 8,
    yref = 'y'
)


st.plotly_chart(fig)