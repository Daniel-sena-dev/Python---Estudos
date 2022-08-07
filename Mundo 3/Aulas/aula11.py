# FUNÇÕES - DEF
# criando uma função
def funContinuar(cont):
    import time
    while True:
        if cont in 'SN':
            break
        else:
            print('Valor invalido')
            cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        print('Finalizando', end='')
        for contador in range(0, 3):
            time.sleep(0.5)
            print('.', end='')
        print()



funContinuar(cont=input('Quer continuar? [S/N] ').upper()[0])
