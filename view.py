import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../persistencia')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../entidades')))

from persistencia.medicos import NMedico
from persistencia.pacientes import NPaciente
from entidades.medico import Medico
from entidades.paciente import Paciente

class View:
    # Paciente CRUD
    @staticmethod
    def Paciente_Listar():
        return NPaciente.Listar()

    @staticmethod
    def Paciente_Inserir(nome, data_nascimento, cpf):
        id_paciente = max([paciente.get_id() for paciente in NPaciente.Listar()], default=0) + 1
        paciente = Paciente(id_paciente, nome, data_nascimento, cpf)
        NPaciente.Inserir(paciente)
        NPaciente.Salvar()

    @staticmethod
    def Paciente_Atualizar(id, nome, data_nascimento, cpf):
        paciente = Paciente(id, nome, data_nascimento, cpf)
        NPaciente.Atualizar(paciente)
        NPaciente.Salvar()

    @staticmethod
    def Paciente_Excluir(id):
        paciente = NPaciente.Listar_Id(id)
        if paciente:
            NPaciente.Excluir(paciente)
            NPaciente.Salvar()

    # Medico CRUD
    @staticmethod
    def Medico_Listar():
        return NMedico.Listar()

    @staticmethod
    def Medico_Inserir(nome, crm, especialidade):
        id_medico = max([medico.get_id() for medico in NMedico.Listar()], default=0) + 1
        medico = Medico(id_medico, nome, crm, especialidade)
        NMedico.Inserir(medico)
        NMedico.Salvar()

    @staticmethod
    def Medico_Atualizar(id, nome, crm, especialidade):
        medico = Medico(id, nome, crm, especialidade)
        NMedico.Atualizar(medico)
        NMedico.Salvar()

    @staticmethod
    def Medico_Excluir(id):
        medico = NMedico.Listar_Id(id)
        if medico:
            NMedico.Excluir(medico)
            NMedico.Salvar()
