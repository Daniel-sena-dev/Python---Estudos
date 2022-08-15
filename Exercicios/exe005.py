def maiorOuIgual(num1, num2):
    if num1 >= num2:
        return True
    else:
        return False


num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
saida = maiorOuIgual(num1, num2)
print(saida)
