import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from persistenciaBase import PersistenciaBase
from entitades.medico import Medico
import json


class NMedico(PersistenciaBase):
    _medicos = []

    def __init__(self):
        super().__init__()
        self._objetos = NMedico._medicos

    def _criar_objeto(self, id, nome, crm, especialidade):
        # Cria o objeto Medico explicitamente
        return Medico(id, nome, crm, especialidade)

    def Abrir(self):
        try:
            with open('medicos.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    # Passa os atributos explicitamente para o método _criar_objeto
                    medico = self._criar_objeto(
                        item['id'], 
                        item['nome'], 
                        item['CRM'], 
                        item['especialidade']
                    )
                    self._objetos.append(medico)
        except FileNotFoundError:
            self._objetos = []

    def Salvar(self):
        super().Salvar('medicos.json')
