mensagem = input('Digite algo: ')
print(f'O tipo primitivo desse valor é \033[0;34;40m{type(mensagem)}\033[0m')
print(f'Só tem espaços? \033[1;33;107m{mensagem.isspace()}\033[0m')
print(f'É um número? \033[1;31;40m{mensagem.isnumeric()}\033[0m')
print(f'É alfabético? \033[1;31;40m{mensagem.isalpha()}\033[0m')
print(f'É alfanumérico? \033[1;31;40m{mensagem.isalnum()}\033[0m')
print(f'Está em maiúsculas? \033[1;31;40m{mensagem.isupper()}\033[0m')
print(f'Está em minúsculas? \033[1;31;40m{mensagem.islower()}\033[0m')
print(f'Está capitalizada? \033[1;31;40m{mensagem.istitle()}\033[0m') #Capitalizada




