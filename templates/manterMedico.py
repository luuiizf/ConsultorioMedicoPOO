import streamlit as st
import pandas as pd
from view import View
import time

class ManterMedicoUI:
    def main():
        st.header("Cadastro de Médicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterMedicoUI.listar()
        with tab2: ManterMedicoUI.inserir()
        with tab3: ManterMedicoUI.atualizar()
        with tab4: ManterMedicoUI.excluir()

    def listar():
        medicos = View.Medico_Listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            dic = []  # lista de dicionários, onde cada dicionário é um médico
            for obj in medicos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do médico")
        crm = st.text_input("Informe o CRM do médico")
        especialidade = st.text_input("Informe a especialidade do médico")
        if st.button("Inserir"):
            View.Medico_Inserir(nome, crm, especialidade)
            st.success("Médico inserido com sucesso")
            time.sleep(2)
            st.experimental_rerun()

    def atualizar():
        medicos = View.Medico_Listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            op = st.selectbox("Atualização de Médicos", medicos, format_func=lambda medico: medico.get_nome())
            nome = st.text_input("Informe o novo nome", op.get_nome())
            crm = st.text_input("Informe o novo CRM", op.get_crm())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Medico_Atualizar(id, nome, crm, especialidade)
                st.success("Médico atualizado com sucesso")
                time.sleep(2)
                st.experimental_rerun()

    def excluir():
        medicos = View.Medico_Listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            op = st.selectbox("Exclusão de Médicos", medicos, format_func=lambda medico: medico.get_nome())
            if st.button("Excluir"):
                id = op.get_id()
                View.Medico_Excluir(id)
                st.success("Médico excluído com sucesso")
                time.sleep(2)
                st.experimental_rerun()
