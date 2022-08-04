reta1 = int(input('Digite o tamanho da primeira reta: '))
reta2 = int(input('Digite o tamanho da segunda reta: '))
reta3 = int(input('Digite o tamanho da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'As retas A={reta1}, B={reta2} e C={reta3} satisfazem a exigencia para existencia de um triangulo')
else:
    print('Não cumpre as exigencias para existencia de um triangulo')