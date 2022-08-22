print('17- programa para saber se um ano é bissexto ou não')
ano = int(input('Digite um ano: '))
if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
