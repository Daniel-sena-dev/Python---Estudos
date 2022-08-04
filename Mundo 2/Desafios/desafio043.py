peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em M: '))
IMC = peso / altura**2

if IMC < 18.5:
    print(f'Seu IMC é de \033[1m{IMC:.02f}\033[m, você está abaixo do peso.')
elif IMC >= 18.5 and IMC < 25:
    print(f'Seu IMC é de \033[1m{IMC:.02f}\033[m, você está no peso ideal.')
elif IMC >= 25 and IMC < 30:
    print(f'Seu IMC é de \033[1m{IMC:.02f}\033[m, você está sobrepeso.')
elif IMC >= 30 and IMC < 40:
    print(f'Seu IMC é de \033[1m{IMC:.02f}\033[m, você está Obeso.')
else:
    print(f'Seu IMC é de \033[1m{IMC:.02f}\033[m, você está com obesidade morbida.')

