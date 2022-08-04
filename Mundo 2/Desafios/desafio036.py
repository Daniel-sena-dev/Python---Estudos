valorCasa = float(input('Digite o valor da sua casa: '))
salarioComprador = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantos anos você pretende parcelar: '))
parcelaAno = valorCasa / anos
parcelaMes = parcelaAno / 12
podePagar = salarioComprador * 0.30

if parcelaMes <= podePagar:
    print(f'Parabens seu emprestimo foi liberado')
    print(f'O valor de anual foi de \033[4mR$ {parcelaAno:.02f}\033[m')
    print(f'O valor mensal de \033[4mR$ {parcelaMes:.02f}\033[m')
else:
    print('O emprestimo nao foi liberado, volte a tentar daqui a dois meses')