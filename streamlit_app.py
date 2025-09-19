import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login_screen():
    st.header('This app is private')
    st.subheader("Please log in")
    st.button("Log in with Google", on_click=st.login)

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login_screen, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")


dashboard = st.Page('pages/dashboard.py', title='Dashboard', icon=':material/dashboard:', default=True)
medical=st.Page('pages/medical.py', title='Medical Encouters', icon=':material/medical_services:')
weight = st.Page('pages/weight.py', title='Weight', icon=':material/monitor_weight:')
vaccines = st.Page('pages/vaccines.py', title="Vaccines", icon=":material/vaccines:")
prescriptions = st.Page('pages/prescriptions.py', title="Prescriptions", icon=':material/medication:')
dental = st.Page('pages/dental.py', title='Dental', icon=':material/dentistry:')
bloodwork = st.Page('pages/bloodwork.py', title="Bloodwork", icon=':material/health_metrics:')
edit = st.Page('pages/edit.py', title='Add Information', icon=':material/edit:')
vets = st.Page('pages/vets.py', title='Vet Information', icon= ':material/stethoscope:')
clinics = st.Page('page/clinics.py', title='Clinic Information', icon= ':material/local_hospital:')



with st.sidebar:
    st.image('images/feline_metrics_logo.png', width=200)


if not st.user.is_logged_in:
    #login_screen()
    pg = st.navigation([login_page])
else:
    st.write(f"Signed in as: {st.user.name}!")
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Mel's Medical Records": [dashboard, medical, weight, vaccines, prescriptions, dental, bloodwork],
            "General Information": [vets, clinics]
            "Add Records": [edit]
        }
    )

pg.run()