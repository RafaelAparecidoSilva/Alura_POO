from restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melância', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()