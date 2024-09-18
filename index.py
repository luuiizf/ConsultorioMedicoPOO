from templates.manterMedico import ManterMedicoUI
from templates.manterPaciente import ManterPacienteUI
from view import View

import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Manter Médicos", "Manter Pacientes"])
        if op == "Manter Médicos":
            ManterMedicoUI.main()
        if op == "Manter Pacientes":
            ManterPacienteUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()
