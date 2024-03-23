from avaliacao import Avaliacao

class Restaurante:
    # Atributos de classe (atributos dentro da função __init__ são os métodos de instância)
    lista_restaurante = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
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
            print(f'Nome: {restaurante._nome.ljust(15)} | Categoria: {restaurante._categoria.ljust(15)} | Avaliação: {str(restaurante.media_avaliacoes).ljust(15)} | Situação: {restaurante.ativo}')
            # print(vars(restaurante))

    @property
    def ativo(self):
        return 'Ativo' if self._ativo == True else 'Inativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        
        return media