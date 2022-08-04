precoProduto = float(input('Digite o preço do produto: '))
print('-=-' * 20)
print(' \033[1m[1] - Á vista dinheiro/cheque: 10% de desconto \n [2] - Á vista no cartão: 5% de desconto \n [3] - Em até 2x no cartão: preço normal \n [4] - Em 3x ou mais no cartão: 20% de juros\033[m')
formaPagamento = int(input('Qual a forma de pagamento? (digite um dos valores informados) '))
print('-=-' * 20)

if formaPagamento == 1:
    print(f'A forma de pagamento selecionada foi [1] - Á vista dinheiro/cheque: 10% de desconto')
    print(f'O valor do produto sem desconto foi de R$ {precoProduto:.02f}.')
    print(f'O valor do produto com desconto ficou em R$ {precoProduto - (precoProduto * 0.10):.02f}')
elif formaPagamento == 2:
    print(f'A forma de pagamento selecionada foi [2] - Á vista no cartão: 5% de desconto')
    print(f'O valor do produto sem desconto foi de R$ {precoProduto:.02f}.')
    print(f'O valor do produto com desconto ficou em R$ {precoProduto - (precoProduto * 0.05):.02f}')
elif formaPagamento == 3:
    print(f'A forma de pagamento selecionada foi [3] - Em até 2x no cartão: preço normal')
    print(f'O valor do produto foi de R$ {precoProduto:.02f}.')
elif formaPagamento == 4:
    print(f'A forma de pagamento selecionada foi [4] - Em 3x ou mais no cartão: 20% de juros')
    parcelas = int(input('Digite quantas parcelas: '))
    precoFinal = (precoProduto + precoProduto*0.20)/parcelas
    print(f'O valor do produto foi de R$ {precoProduto + precoProduto*0.20:.02f}, divido em {parcelas} parcelas ficou R$ {precoFinal:.02f}.')

else:
    print('A forma de pagamento selecionada não é válida.')