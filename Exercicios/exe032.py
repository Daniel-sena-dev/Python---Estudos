print('8- produto mais barato')
produto = [float(input('Digite o valor do produto 1: ')), float(input('Digite o valor do produto 2: ')),
           float(input('Digite o valor do produto 3: '))]
print(f'O produto que você deve comprar é R${min(produto):.02f}')
