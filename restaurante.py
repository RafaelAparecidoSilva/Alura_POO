class Restaurante:
    # Atributos de classe (atributos dentro da função __init__ são os métodos de instância)
    lista_restaurante = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.lista_restaurante.append(self)

    # def __str__(self):
    #     dicionario = {'nome': self.nome, 'categoria': self.categoria, 'Status': 'Ativo' if self.ativo == False else 'Inativo'}
    #     return str(dicionario)
    
    def __str__(self):
        texto = str(vars(self))
        return texto
    
    @classmethod
    def listar_restaurante(cls):
        for restaurante in cls.lista_restaurante:
            print(f'Nome: {restaurante._nome.ljust(15)} | Categoria: {restaurante._categoria.ljust(15)} | Situação: {restaurante.ativo}')
            # print(vars(restaurante))

    @property
    def ativo(self):
        return 'Ativo' if self._ativo == True else 'Inativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


if __name__ == "__main__":
    restaurante1 = Restaurante('Bistrô', 'Fast Food')
    restaurante2 = Restaurante('Outback', 'Food')
    
    Restaurante.listar_restaurante()
    restaurante1.alternar_estado()
    print('-='*35)
    Restaurante.listar_restaurante()