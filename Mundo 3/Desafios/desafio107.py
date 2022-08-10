import modulos


preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é {modulos.metade(preco)}')
print(f'O dobro de {preco} é {modulos.dobro(preco)}')
print(f'Aumentando 10%, temos {modulos.aumentando(preco)}')
print(f'Diminuindo 15%, temos {modulos.diminuindo(preco)}')
