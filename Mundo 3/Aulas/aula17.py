def contador (inicio, fim, passo):
    """
    -> FAZ I,A CONTAGEM E MOSTRA NA TELA

    :param inicio: do passo
    :param fim: do passo
    :param passo: a passo
    :return: sem retorno
    """
    for cont in range(inicio, fim, passo):
        print(cont)

#contador(int(input('Digite um numero')), int(input('Digite um numero')), int(input('Digite um numero')))

help(contador)