#LISTAS

lista = [0, 1, 2, 3, 4]
print(lista)
lista[2]=5
print(lista)
lista.append(6) #adiciona ao final da lista um item
print(lista)
lista.insert(0, 13) #insire um item onde é pedido
print(lista)
del lista[3] #deleta um item da lista
lista.pop(4) #deleta o ultimo item da lista (pode alterar o index)
lista.remove(6) #remove o conteudo pedido da lista
print(lista)


valores = list(range(4,11)) #cria uma lista num range de 4 a 11
print(valores)
valores.sort(reverse=True) #organiza ou inverte a lista
print(valores)
print(len(valores))

