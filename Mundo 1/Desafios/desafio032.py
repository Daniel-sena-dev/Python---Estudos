import datetime

ano = int(input('Digite um ano para saber se é bissexto ou digite 0 para o ano atual: '))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano% 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é um ano bissexto')

