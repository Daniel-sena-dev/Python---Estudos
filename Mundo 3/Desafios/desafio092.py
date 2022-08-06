import datetime

dados = dict()
anoAtual = datetime.date.today().year

dados['nome'] = input('Nome: ')
anoNascimento = int(input('Ano de Nascimento: '))
dados['idade'] = anoAtual - anoNascimento
carteiraTrabalho = int(input('Carteira de Trabalho (0 não tem): '))
if carteiraTrabalho == 0:
    dados['ctps'] = 0
else:
    dados['ctps'] = carteiraTrabalho
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (35 - (anoAtual - dados['contratação'])) + dados['idade']

for chaves, valores in dados.items():
    print(f'{chaves} tem o valor {valores}')