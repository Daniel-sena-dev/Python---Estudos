# PARAMETRO OPCIONAL
def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(2, 3, 5)
somar(1, 4)


# ESCOPO DE UMA VARIAVEL
def teste():
    global a # VAI UTILIZAR O A VARIVEL GLOBAL AO INVES DE CRIAR UMA NOVA VARIAVEL
    x = 8  # VARIAVEL LOCAL
    print(x)
    print(a)


a = 5  # VARIAVEL GLOBAL
