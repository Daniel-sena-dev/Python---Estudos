print('25- programa 5 perguntas: ')
numeroCrimes = 0

pergunta = str(input('Telefonou para a vítima? Sim ou Não?')).upper()[0]
if pergunta == 'S':
    numeroCrimes += 1
pergunta = str(input('Esteve no local do crime? ')).upper()[0]
if pergunta == 'S':
    numeroCrimes += 1
pergunta = str(input('Mora perto da vítima? ')).upper()[0]
if pergunta == 'S':
    numeroCrimes += 1
pergunta = str(input('Devia para vítima? ')).upper()[0]
if pergunta == 'S':
    numeroCrimes += 1
pergunta = str(input('Já trabalho com a títima? ')).upper()[0]
if pergunta == 'S':
    numeroCrimes += 1

if numeroCrimes == 2:
    print(f'A pessoa respondeu positivamente a {numeroCrimes}, se tornou um suspeito')
elif 3 <= numeroCrimes <= 4:
    print(f'A pessoa respondeu positivamente a {numeroCrimes}, se tornou um cúmplice')
elif numeroCrimes == 5:
    print(f'A pessoa respondeu positivamente a {numeroCrimes}, se tornou um assassino')
else:
    print(f'A pessoa respondeu positivamente a {numeroCrimes}, se é inocente')
