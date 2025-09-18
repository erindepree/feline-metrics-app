import streamlit as st

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


dashboard = st.Page('mel.py', title='Dashboard', icon=':material/dashboard:', default=True)
medical=st.Page('medical.py', title='Medical Encouters', icon=':material/medical_services:')
weight = st.Page('weight.py', title='Weight', icon=':material/monitor_weight:')
vaccines = st.Page('vaccines.py', title="Vaccines", icon=":material/vaccines:")
prescriptions = st.Page('prescriptions.py', title="Prescriptions", icon=':material/medication:')
dental = st.Page('dental.py', title='Dental', icon=':material/dentistry:')
edit = st.Page('edit.py', title='Add Information', icon=':material/edit:')


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Mel's Medical Records": [dashboard, medical, weight, vaccines, prescriptions, dental],
            "Add Records": [edit]
        }
    )
else:
    pg = st.navigation([login_page])


pg.run()