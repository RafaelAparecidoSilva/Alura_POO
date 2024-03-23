from restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Rafael', 9)
restaurante_praca.receber_avaliacao('Ana', 4)
restaurante_praca.receber_avaliacao('Gomes', 10)



def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()