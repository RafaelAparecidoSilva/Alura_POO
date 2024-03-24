## Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

## Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

## Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

## Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

class Livro:

    lista_livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_livros.append(self)

    def __str__(self):
        return f'Título: {self._titulo.ljust(15)} | Autor: {self._autor.ljust(10)} | Ano da Publicação: {str(self._ano_publicacao).ljust(5)} | Disponibilidade: {self.disponivel}'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel == True else 'Indisponível'
    
    @staticmethod
    def verificar_disponibilidade(ano):
        lista_disponibilidade = []

        for livro in Livro.lista_livros:
            if livro._ano_publicacao == ano:
                lista_disponibilidade.append(livro._titulo)
        
        return sorted(lista_disponibilidade)




if __name__ == '__main__':
    livro1 = Livro('Crepusculo', 'David', 2023)
    livro2 = Livro('Morte Severina', 'Claudio', 2024)
    livro3 = Livro('Noturno', 'San', 2023)
    livro1.emprestar()

    res = Livro.verificar_disponibilidade(2023)
    print('Livros disponíveis: ', res)

    print('-='*35)
    print(livro1)
    print(livro2)
    print(livro3)
    print('-='*35)