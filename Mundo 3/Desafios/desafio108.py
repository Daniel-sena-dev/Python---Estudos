import modulos

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {modulos.moeda(preco)} é {modulos.moeda(modulos.metade(preco))}')
print(f'O dobro de {modulos.moeda(preco)} é {modulos.moeda(modulos.dobro(preco))}')
print(f'Aumentando 10%, temos {modulos.moeda(modulos.aumentando(preco))}')
print(f'Diminuindo 15%, temos {modulos.moeda(modulos.diminuindo(preco))}')
