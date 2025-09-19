import streamlit as st

st.set_page_config(
    page_title = "FelineMetrics | Mel",
    page_icon = ":material/dashboard:"
)

st.title(":material/dashboard: FelineMetrics | Mel | Dashboard")

st.write("Link to: weight figure, list of medical appointments, list of vaccines, dental, prescriptions, etc.")

row1 = st.container(horizontal=True, horizontal_alignment='center')

row1.page_link("pages/medical.py", label="Medical Encounters", icon= ":material/local_hospital:")
row1.page_link("pages/weight.py", label="Medical Encounters", icon= ":material/monitor_weight:")
row1.page_link("pages/vaccines.py", label="Vaccines", icon= ":material/vaccines:")
row1.page_link("pages/prescriptions.py", label="Prescriptions", icon= ":material/medication:")
row1.page_link("pages/dental.py", label="Dental Care", icon= ":material/dentistry:")
row1.page_link("pages/bloodwork.py", label="Bloodwork Results", icon= ":material/health_metrics:")
