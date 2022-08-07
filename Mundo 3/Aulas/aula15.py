def soma(*num):
    s = 0
    for contador in num:
        s += contador
    print(f'O valor de soma de {num} é igual a {s}')




soma(0, 5, 7)