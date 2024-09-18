import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from persistenciaBase import PersistenciaBase
from entitades.paciente import Paciente

import json

class NPaciente(PersistenciaBase):
    _pacientes = []

    def __init__(self):
        super().__init__()
        self._objetos = NPaciente._pacientes

    def _criar_objeto(self, id, nome, cpf, data_nascimento, senha):
        # Cria o objeto Paciente explicitamente
        return Paciente(id, nome, cpf, data_nascimento, senha)

    def Abrir(self):
        try:
            with open('pacientes.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    # Passa os atributos explicitamente para o método _criar_objeto
                    paciente = self._criar_objeto(
                        item['id'], 
                        item['nome'], 
                        item['cpf'], 
                        item['data_nascimento'], 
                        item['senha']
                    )
                    self._objetos.append(paciente)
        except FileNotFoundError:
            self._objetos = []

    def Salvar(self):
        super().Salvar('pacientes.json')
