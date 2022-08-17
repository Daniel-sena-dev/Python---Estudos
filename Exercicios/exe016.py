def soma(lista):
    saida = 0
    for contador in lista:
        saida += contador
    return saida


lista = [15, 10, 10]
retorno = soma(lista)
print(retorno)

