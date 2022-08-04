numero = int(input('Digite um numero: '))
conversao = int(input('Qual conversão você deseja? \n1 - Para binário \n2 - Para octal \n3 - Para hexadecimal '))

#bin() converte um numero inteiro para binario

if conversao == 1:
    print(f'O numero digitado foi \033[4m{numero}\033[m é sua forma binaria é de \033[4m{numero:b}\033[m')
elif conversao == 2:
    print(f'O numero digitado foi \033[4m{numero}\033[m é sua forma octal é de \033[4m{numero:o}\033[m')
elif conversao == 3:
    print(f'O numero digitado foi \033[4m{numero}\033[m é sua forma hexadecimal é de \033[4m{hex(numero)[2:]}\033[m')
else:
    print('O numero digitado nao corresponde a nenhuma conversao.')