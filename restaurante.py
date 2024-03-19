class Restaurante:
    # Atributos de classe (atributos dentro da função __init__ são os métodos de instância)
    lista_restaurante = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.lista_restaurante.append(self)

    # def __str__(self):
    #     dicionario = {'nome': self.nome, 'categoria': self.categoria, 'Status': 'Ativo' if self.ativo == False else 'Inativo'}
    #     return str(dicionario)
    
    def __str__(self):
        texto = str(vars(self))
        return texto
    
    def listar_restaurante():
        for restaurante in Restaurante.lista_restaurante:
            print(f'Nome: {restaurante.nome.ljust(15)} | Categoria: {restaurante.categoria.ljust(15)} | Situação: {restaurante.ativo}')
            # print(vars(restaurante))

    @property
    def ativo(self):
        return 'Ativo' if self._ativo == True else 'Inativo'


if __name__ == "__main__":
    restaurante1 = Restaurante('Bistrô', 'Fast Food')
    restaurante2 = Restaurante('Outback', 'Food')

    Restaurante.listar_restaurante()
    