print('11- Programa para aumento dos salarios: ')
salario = float(input('Digite o salario do funcionario: '))
reajusteSalarial = 0
salarioTotal = 0

if salario < 280:
    reajusteSalarial = salario * 0.2
    salarioTotal = salario + reajusteSalarial
    print(f'O salario atual do funcionario: R${salario:.02f}')
    print(f'O aumento vai ser de 20%')
    print(f'O aumento vai ser R${reajusteSalarial:.02f}')
    print(f'O salario final será de: R${salarioTotal:.02f}')
elif 280 <= salario < 700:
    reajusteSalarial = salario * 0.15
    salarioTotal = salario + reajusteSalarial
    print(f'O salario atual do funcionario: R${salario:.02f}')
    print(f'O aumento vai ser de 15%')
    print(f'O aumento vai ser R${reajusteSalarial:.02f}')
    print(f'O salario final será de: R${salarioTotal:.02f}')
elif 700 <= salario < 1500:
    reajusteSalarial = salario * 0.1
    salarioTotal = salario + reajusteSalarial
    print(f'O salario atual do funcionario: R${salario:.02f}')
    print(f'O aumento vai ser de 10%')
    print(f'O aumento vai ser R${reajusteSalarial:.02f}')
    print(f'O salario final será de: R${salarioTotal:.02f}')
else:
    reajusteSalarial = salario * 0.05
    salarioTotal = salario + reajusteSalarial
    print(f'O salario atual do funcionario: R${salario:.02f}')
    print(f'O aumento vai ser de 5%')
    print(f'O aumento vai ser R${reajusteSalarial:.02f}')
    print(f'O salario final será de: R${salarioTotal:.02f}')