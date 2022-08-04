
#Variaveis
import time

nomeProduto = ''
preco = 0
continuar = ''
menorPreco = 0
totalGasto = 0
produtoAcimaMil = 0
produtoMaisBarato = ''
quantidadeProdutos = 0

while True:
    print('-=-' * 10)
    nomeProduto = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: R$ '))
    #VALIDANDO O PREÇO
    while preco < 0:
        print('Preço digitado invalido!')
        preco = float(input('Digite o valor do produto: R$ '))
    print('-=-' * 10)
    quantidadeProdutos += 1

    #ORGANIZANDO OS DADOS==========================
    #Total gasto
    totalGasto += preco

    #PRODUTO QUE CUSTA MAIS DE R$1000
    if preco > 1000:
        produtoAcimaMil += 1

    #PREÇO MAIS ALTO
    if quantidadeProdutos == 1:
        menorPreco = preco
        produtoMaisBarato = nomeProduto
    elif preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = nomeProduto

    #==============================================
    #Perguntando se deseja continuar
    continuar = input('Deseja continuar? Digite sim ou não [S/N] ').upper()
    #Validando a resposta
    while continuar != 'S' and continuar != 'N':
        print('\033[1;32mValor digitado invalido! digite novamente\033[m')
        continuar = input('Deseja continuar? digite sim ou não [S/N] ').upper()

    if continuar == 'N':
        print('Finalizando', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        break

print(f'O valor total de suas compras deu R${totalGasto:.02f}')
print(f'Os produtos avaliados acima de R$1000 foi de {produtoAcimaMil}')
print(f'O produto mais barato foi {produtoMaisBarato} e o seu valor foi de R${menorPreco:.02f}')