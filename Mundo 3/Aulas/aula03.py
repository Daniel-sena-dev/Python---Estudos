#LISTAS 1
numero = [2, 5, 9, 1]
print(numero)
numero.append(7)
numero.sort(reverse=True)
numero.insert(2, 0)
print(numero)
print(f'Essa lista tem {len(numero)} elementos.')
numero.pop(1)
print(numero)

for contador, valores in enumerate(numero):
    print((f'Na posição {contador} encontrei o valor {valores}! '))
print('Fim da lista')

#==============================================================
a = [2, 3, 4, 5]
#b = a #cria uma copia
b = a[:]
b[2] = 9
print(a)
print(b)
