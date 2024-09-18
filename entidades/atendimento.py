from paciente import Paciente
from medico import Medico

import datetime

class Atendimento:
    def __init__(self, id, data_hora, id_medico, id_paciente, id_procedimento, confirmado):
        self.__id = id
        self.__data_hora = datetime.now()
        self.__id_medico = id_medico
        self.__id_paciente = id_paciente
        self.__id_procedimento = id_procedimento
        self.__confirmado = confirmado

    def get_id(self):
        return self.__id

    def get_data_hora(self):
        return self.__data_hora

    def get_id_medico(self):
        return self.__id_medico

    def get_id_paciente(self):
        return self.__id_paciente

    def get_id_procedimento(self):
        return self.__id_procedimento

    def get_confirmado(self):
        return self.__confirmado


    def set_id(self, id):
        self.__id = id

    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora

    def set_id_medico(self, id_medico):
        self.__id_medico = id_medico

    def set_id_paciente(self, id_paciente):
        self.__id_paciente = id_paciente

    def set_id_procedimento(self, id_procedimento):
        self.__id_procedimento = id_procedimento

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def Consulta(self, consulta, id, data, hora, medico, paciente):
        print(f"Consulta marcada com ID: {id}")
        print(f"Data: {data.strftime('%d/%m/%Y')}, Hora: {hora.strftime('%H:%M')}")
        print(f"Médico: {medico}")
        print(f"Paciente: {paciente}")
        return consulta

