import json

class PersistenciaBase:
    def __init__(self):
        self._objetos = []

    def Inserir(self, obj):
        self._objetos.append(obj)

    def Listar(self):
        return self._objetos

    def Listar_Id(self, id):
        for obj in self._objetos:
            if obj.get_id() == id:
                return obj
        return None

    def Atualizar(self, obj):
        for i, item in enumerate(self._objetos):
            if item.get_id() == obj.get_id():
                self._objetos[i] = obj
                break

    def Excluir(self, obj):
        self._objetos = [item for item in self._objetos if item.get_id() != obj.get_id()]

    def Abrir(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                data = json.load(file)
                self._objetos = [self._criar_objeto(**item) for item in data]
        except FileNotFoundError:
            self._objetos = []

    def Salvar(self, arquivo):
        with open(arquivo, 'w') as file:
            data = [obj.__dict__ for obj in self._objetos]
            json.dump(data, file, default=str)

    # Método abstrato a ser implementado nas classes específicas
    def _criar_objeto(self, **kwargs):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")
