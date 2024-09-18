from usuario import Usuario
from datetime import datetime

class Paciente(Usuario):
    def __init__(self, id, nome, cpf, data_nascimento, senha):
        super().__init__(id, nome)
        self._cpf = cpf
        self.set_data_nascimento(data_nascimento)
        self._senha = senha
    
    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, cpf):
        self._cpf = cpf
    
    def get_data_nascimento(self):
        return self._data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        if isinstance(data_nascimento, str):
            # Converte a string para datetime no formato DD-MM-YYYY
            try:
                self._data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y")
            except ValueError:
                raise ValueError("Data de nascimento inválida. Use o formato DD-MM-YYYY.")
        elif isinstance(data_nascimento, datetime):
            self._data_nascimento = data_nascimento
        else:
            raise TypeError("Data de nascimento deve ser uma string ou um objeto datetime.")
    
    def get_senha(self):
        return self._senha
    
    def set_senha(self, senha):
        self._senha = senha
    
    def __str__(self):
        return f"Paciente (ID: {self._id}, Nome: {self._nome}, CPF: {self._cpf}, Data de Nascimento: {self._data_nascimento.strftime('%d-%m-%Y')}, Senha: [Oculta])"
