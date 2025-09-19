import streamlit as st

st.set_page_config(
    page_title = "FelineMetrics | Dental Care",
    page_icon = ":material/dentistry:"
)

st.title(":material/dentistry: Mel's Dental Care")

st.write("List dental services, notes, etc")

#df_dental = pd.read_csv