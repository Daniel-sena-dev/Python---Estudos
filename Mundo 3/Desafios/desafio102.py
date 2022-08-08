def fatorial(numero, show=False):
    """
    :param numero: numero que voce quer o fatorial
    :param show: quer que mostre como calcular o fatorial?
    :return: fatorial
    """
    fat = numero
    total = numero
    if show:
        print('-' * 30)
        print(f'{fat} x ', end='')
        for contador in range(1, numero):
            if contador >= numero - 1:
                fat -= 1
                total *= fat
                print(f'{fat} = ', end='')
            else:
                fat -= 1
                total *= fat
                print(f'{fat} x ', end='')
        print(total)
    else:
        for contador in range(0, numero - 1):
            fat -= 1
            total *= fat
        print(total)


#help(fatorial)
fatorial(3, True)
