from usuario import Usuario

class Medico(Usuario):
    def __init__(self, id, nome, CRM, especialidade):
        super().__init__(id, nome)
        self._CRM = CRM
        self._especialidade = especialidade
    
    def get_CRM(self):
        return self._CRM
    
    def set_CRM(self, CRM):
        self._CRM = CRM
    
    def get_especialidade(self):
        return self._especialidade
    
    def set_especialidade(self, especialidade):
        self._especialidade = especialidade
    
    def emitir_Receita(self):
        # Implementação da emissão de receita
        pass
    
    def __str__(self):
        return f"Medico (ID: {self._id}, Nome: {self._nome}, CRM: {self._CRM}, Especialidade: {self._especialidade})"
