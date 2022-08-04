preco = float(input('Digite o preço do produto: '))
desconto = 0.05
valorDesconto = preco * desconto

print(f'O valor do produto é de R${preco:.02f}, o valor de 5% de desconto é de R${valorDesconto:.02f} o valor com desconto é de R${preco - valorDesconto:.02f}')