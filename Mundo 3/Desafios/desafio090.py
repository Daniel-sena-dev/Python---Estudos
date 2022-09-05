aluno = dict()

aluno['Nome'] = input('Digite o nome do aluno: ')
aluno['Media'] = float(input(f'Digite a mediaVeiculos de {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for chaves, valores in aluno.items():
    print(f'{chaves} é igual a {valores}')
