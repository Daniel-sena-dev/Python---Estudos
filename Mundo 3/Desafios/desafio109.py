import modulos


preco = float(input('Digite o preço: R$ '))
print(f'A metade de {modulos.moeda(preco)} é {modulos.metade(preco, True)}')
print(f'O dobro de {modulos.moeda(preco)} é {modulos.dobro(preco, True)}')
print(f'Aumentando 10%, temos {modulos.aumentando(preco, True)}')
print(f'Diminuindo 15%, temos {modulos.diminuindo(preco, True)}')