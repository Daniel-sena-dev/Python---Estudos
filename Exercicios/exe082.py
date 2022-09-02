print('30- programa para tabela de preços: 2.0v')
preco = float(input('Digite o preço do pão: '))

print('Panificadora Pão de Ontem - Tabela de preços')
for cont in range(0, 50):
    print(f'{cont + 1} - R$ {preco * (cont + 1):.02f}')
