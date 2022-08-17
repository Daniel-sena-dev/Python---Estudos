def receberSomenteOsParesDeIndicesPares(pares):
    listaPares = list()
    for contador in range(0, len(pares)):
        if contador % 2 == 0:
            if pares[contador] % 2 == 0:
                listaPares.append(pares[contador])
    return listaPares


lista = [10, 70, 22, 43]
saida = receberSomenteOsParesDeIndicesPares(lista)
print(saida)
