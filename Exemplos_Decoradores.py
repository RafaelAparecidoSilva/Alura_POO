"""
O decorator @property é uma ferramenta útil em Python que permite transformar um método de uma classe em um atributo de leitura (ou getter). Isso significa que você pode acessar esse método como se fosse um atributo da instância, sem a necessidade de usar parênteses para chamá-lo como um método regular.

Ao decorar um método com @property, você cria uma propriedade computada, ou seja, uma propriedade que é calculada dinamicamente com base em outros atributos da instância. Isso é útil quando você deseja encapsular a lógica de cálculo de um atributo, mantendo a interface de acesso consistente para o usuário da classe."""


class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def area(self):
        return self._largura * self._altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor <= 0:
            raise ValueError("A largura deve ser um valor positivo")
        self._largura = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("A altura deve ser um valor positivo")
        self._altura = valor

# Uso da classe Retangulo
retangulo = Retangulo(5, 10)
print(retangulo.area)  # Saída: 50

retangulo.largura = 6
retangulo.altura = 12
print(retangulo.area)  # Saída: 72


"""
Neste exemplo, a classe Retangulo possui os atributos _largura e _altura. Os métodos largura e altura são decorados com @property, o que os torna acessíveis como atributos de leitura. Além disso, os métodos largura e altura também têm métodos setters correspondentes decorados com @largura.setter e @altura.setter, respectivamente, o que permite definir os valores desses atributos com validação. Isso oferece uma maneira mais controlada de manipular os atributos da classe.
"""