# EMPACOTANDO PARAMETROS
def contador(*num):
    for i in num:
        print(f'{i} ', end='')
    print('FIM!')


contador(2, 3, 5, 10)

