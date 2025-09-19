import streamlit as st

st.set_page_config(
    page_title = "FelineMetrics | Dashboard",
    page_icon = ":material/dashboard:"
)

st.title(":material/dashboard: Mel's Dashboard")


st.header("Mel's Medical Records")

row1 = st.container(horizontal=True, horizontal_alignment='center')
row2 = st.container(horizontal=True, horizontal_alignment='center')

row1.page_link("pages/medical.py", label="Medical Encounters", icon= ":material/local_hospital:")
row1.page_link("pages/weight.py", label="Medical Encounters", icon= ":material/monitor_weight:")
row1.page_link("pages/vaccines.py", label="Vaccines", icon= ":material/vaccines:")

row2.page_link("pages/prescriptions.py", label="Prescriptions", icon= ":material/medication:")
row2.page_link("pages/dental.py", label="Dental Care", icon= ":material/dentistry:")
row2.page_link("pages/bloodwork.py", label="Bloodwork Results", icon= ":material/health_metrics:")


st.header(General Information)

row3 = st.container(horizontal=True, horizontal_alignment='center')

row3.page_link("pages/vets.py", label="Vet Info", icon= ":material/stethoscope:")
row3.page_link("pages/clinics.py", label="Clinic Info", icon= ":material/local_hospital:")