import datetime
maioresIdade = 0
menoresIdade = 0
anoAtual = datetime.date.today().year
pessoas = 7

for contador in range(0, pessoas):
    anoNascimento = int(input('Digite o ano de nascimento: '))
    if (anoAtual - anoNascimento >= 21):
        maioresIdade += 1
    else:
        menoresIdade += 1

print(f'{maioresIdade} são maiores de idade! {menoresIdade} são menores de idade! ')