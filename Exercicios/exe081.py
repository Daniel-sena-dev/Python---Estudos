print('29- programa para tabela de preços: ')
preco = 1.99
print('Lojas Quase Dois - Tabela de preços')
for cont in range(0, 50):
    print(f'{cont + 1} - R$ {preco * (cont + 1):.02f}')
