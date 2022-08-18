# TESTE
lataTinta18 = 18
lataTinta36 = 3.6
parede = 250 / 6
print(f'TOTAL QUE PRECISA PARA PAREDE {parede:.02f}')
total18 = parede // lataTinta18
resto = parede % lataTinta18
print(f'{resto:.02f}')
print(f'TOTAL DE LATAS 18 QUE PRECISA {total18}')

total36 = resto // lataTinta36

print(f'TOTAL DE LATAS 3,6 QUE PRECISA {total36}')

