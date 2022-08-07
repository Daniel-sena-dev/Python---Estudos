def dobra(lista):
    for contador in range(0, len(lista)):
        lista[contador] = lista[contador] * 2
    print(lista)


# Programa principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
