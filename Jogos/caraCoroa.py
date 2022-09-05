import random
import modulos

modulos.menus('CARA OU COROA')
sair = False

while True:
    jogadas = ['CARA', 'COROA']
    jogadaPc = random.randint(0, 1)
    if sair:
        break

    while True:
        try:
            caraCoroa = str(input('Digite cara ou coroa (digite sair para desistir): ')).upper()
        except ValueError:
            print('Erro! valor invalido')
        else:
            if caraCoroa == 'CARA' or caraCoroa == 'COROA':
                break
            elif caraCoroa == 'SAIR':
                sair = True
                break

    if caraCoroa == jogadas[jogadaPc] and sair == False:
        print('Você ganhou!')
    else:
        print('Você perdeu!')

