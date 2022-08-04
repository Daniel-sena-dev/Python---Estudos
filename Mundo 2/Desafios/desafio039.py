import datetime

print('-=-' * 20)
anoNascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    print('Você é menor de 18 anos, ainda não chegou sua hora de se alistar!')
    print(f'Faltam \033[1m{18 - idade}\033[m anos para você se apresentar')
elif idade == 18:
    print('Pode se apresentar para o alistamento')
else:
    print('Já passou o tempo de você se apresentar!')
    print(f'Você ja está \033[1m{idade - 18}\033[m anos atrasado!')

