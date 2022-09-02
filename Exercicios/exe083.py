print('31- programa para tabela de preços: 3.0v')
total = 0
finalizar = False
dinheiro = float(input('Digite quanto você tem: '))


while True:
    quantProdutos = 1
    while True:
        try:
            preco = float(input(f'Digite o preço do produto {quantProdutos}: '))
        except ValueError:
            print('ERRO! Valor invalido')
        else:
            if preco == 0:
                finalizar = True
                break
            else:
                print(f'Produto {quantProdutos}: R$ {preco:.02f}')
                total += preco
                quantProdutos += 1
    if finalizar:
        break

print(f'Total: R${total:.02f}')
print(f'Dinheiro: R${dinheiro:.02f}')
print(f'Troco: R${dinheiro-total:.02f}')
