from usuario import Usuario

class Procedimento(Usuario):
    def __init__(self, id, nome, valor):
        super().__init__(id, nome)
        self.__valor = valor

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def __str__(self):
        return f"ID: { self.__id }\n NOME: { self.__nome }\n VALOR: R${self.__valor}"
    
    