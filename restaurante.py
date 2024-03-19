class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    # def __str__(self):
    #     dicionario = {'nome': self.nome, 'categoria': self.categoria, 'Status': 'Ativo' if self.ativo == False else 'Inativo'}
    #     return str(dicionario)
    
    def __str__(self):
        texto = str(vars(self))
        return texto


if __name__ == "__main__":
    restaurante = Restaurante('Bistrô', 'Fast Food')
    print(restaurante)