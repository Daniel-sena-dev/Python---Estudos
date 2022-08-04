import datetime

anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print(f'O atleta tem \033[4m{idade}\033[m anos, vai competir na categoria \033[1mmirim\033[m')
elif idade <= 14:
    print(f'O atleta tem \033[4m{idade}\033[m anos, vai competir na categoria \033[1minfantil\033[m')
elif idade <= 19:
    print(f'O atleta tem \033[4m{idade}\033[m anos, vai competir na categoria \033[1mjunior\033[m')
elif idade <= 20:
    print(f'O atleta tem \033[4m{idade}\033[m anos, vai competir na categoria \033[1msênior\033[m')
else:
    print(f'O atleta tem \033[4m{idade}\033[m anos, vai competir na categoria \033[1mmaster\033[m')