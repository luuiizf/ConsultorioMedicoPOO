class Usuario:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
    
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def __str__(self):
        return f"Usuário (ID: {self._id}, Nome: {self._nome})"
