def estaEntre(num1, min, max, inclusivo=False):
    if min > num1 < max and inclusivo == False:
        return True
    elif min >= num1 <= max and inclusivo == True:
        return True
    else:
        return False


num1 = int(input('Digite um numero: '))
min = int(input('Digite um numero: '))
max = int(input('Digite um numero: '))
saida = estaEntre(num1, min, max, True)
print(saida)
