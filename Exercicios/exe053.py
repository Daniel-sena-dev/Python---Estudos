# Exercicios de estrutura de repetição do site python Brasil
print('1- Programa para pedir nota: ')
num = -1

while True:
    try:
        num = int(input('Digite uma nota de 0 a 10: '))
    except ValueError:
        print(f'Valor invalido')
    else:
        if 0 < num <= 10:
            break
        else:
            print('ERRO! numero digitado invalido')
print(f'A nota digitada foi {num}')
