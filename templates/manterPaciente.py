import streamlit as st
import pandas as pd
from view import View
import time

class ManterPacienteUI:
    def main():
        st.header("Cadastro de Pacientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPacienteUI.listar()
        with tab2: ManterPacienteUI.inserir()
        with tab3: ManterPacienteUI.atualizar()
        with tab4: ManterPacienteUI.excluir()

    def listar():
        pacientes = View.Paciente_Listar()
        if len(pacientes) == 0:
            st.write("Nenhum paciente cadastrado")
        else:
            dic = []  # lista de dicionários, onde cada dicionário é um paciente
            for obj in pacientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do paciente")
        cpf = st.text_input("Informe o CPF do paciente")
        data_nascimento = st.text_input("Informe a data de nascimento do paciente (dd/mm/yyyy)")
        senha = st.text_input("Informe a senha")
        if st.button("Inserir"):
            View.Paciente_Inserir(nome, cpf, data_nascimento, senha)
            st.success("Paciente inserido com sucesso")
            time.sleep(2)
            st.experimental_rerun()

    def atualizar():
        pacientes = View.Paciente_Listar()
        if len(pacientes) == 0:
            st.write("Nenhum paciente cadastrado")
        else:
            op = st.selectbox("Atualização de Pacientes", pacientes, format_func=lambda paciente: paciente.get_nome())
            nome = st.text_input("Informe o novo nome", op.get_nome())
            cpf = st.text_input("Informe o novo CPF", op.get_cpf())
            data_nascimento = st.text_input("Informe a nova data de nascimento", op.get_data_nascimento())
            senha = st.text_input("Informe a nova senha", op.get_senha())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Paciente_Atualizar(id, nome, cpf, data_nascimento, senha)
                st.success("Paciente atualizado com sucesso")
                time.sleep(2)
                st.experimental_rerun()

    def excluir():
        pacientes = View.Paciente_Listar()
        if len(pacientes) == 0:
            st.write("Nenhum paciente cadastrado")
        else:
            op = st.selectbox("Exclusão de Pacientes", pacientes, format_func=lambda paciente: paciente.get_nome())
            if st.button("Excluir"):
                id = op.get_id()
                View.Paciente_Excluir(id)
                st.success("Paciente excluído com sucesso")
                time.sleep(2)
                st.experimental_rerun()
