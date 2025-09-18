import streamlit as st

st.image('images/feline_metrics_logo.png', width=200)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")


dashboard = st.Page('pages/mel.py', title='Dashboard', icon=':material/dashboard:', default=True)
medical=st.Page('pages/medical.py', title='Medical Encouters', icon=':material/medical_services:')
weight = st.Page('pages/weight.py', title='Weight', icon=':material/monitor_weight:')
vaccines = st.Page('pages/vaccines.py', title="Vaccines", icon=":material/vaccines:")
prescriptions = st.Page('pages/prescriptions.py', title="Prescriptions", icon=':material/medication:')
dental = st.Page('pages/dental.py', title='Dental', icon=':material/dentistry:')
bloodwork = st.Page('pages/boodword.py', title="Bloodwork", icon=':material/health_metrics:')
edit = st.Page('pages/edit.py', title='Add Information', icon=':material/edit:')


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Mel's Medical Records": [dashboard, medical, weight, vaccines, prescriptions, dental, bloodwork],
            "Add Records": [edit]
        }
    )
else:
    pg = st.navigation([login_page])


pg.run()