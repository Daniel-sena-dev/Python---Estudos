#TUPLAS
#AS TUPLAS SÃO IMUTÁVEIS
"""
tuplas = ('item1', 'item2', 'item3')
lista = ['item1', 'item2', 'item3')
dicionario = {'item1', 'item2', 'item3'}
"""

lanche = ('Hamburguer', 'suco', 'Pizza', 'Pudim')
print(lanche[2]) #na hora de referenciar sempre utilizar []
print(lanche[0:2])
print(len(lanche))

for pos, contador in enumerate(lanche):
    print(contador)
    print(pos)

print('\n')


for contador in range(0, len(lanche)):
    print(lanche[contador])

#organizando a tupla
print(sorted(lanche))

#=============================
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(c.count(5))
print(c.index(5,1))
#==============================
pessoa = ('Daniel', 23, 'M', 103)
#del(tupla) apaga a tupla toda
print(pessoa)
