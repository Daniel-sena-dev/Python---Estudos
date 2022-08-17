def filtrarNumeros(lista):
    for contador in range(0, len(lista)):
        try:
            int(lista[contador])
        except:
            del lista[contador]
        else:
            lista[contador] = int(lista[contador])
            continue


numeros = [1, '3', 5, 'aaaaa']
filtrarNumeros(numeros)
print(numeros)
