print('28- calcular coleção de cds: '  )
quantidadeCD = int(input('Digite a quantidade de cds: '))
media = 0

for cont in range(0, quantidadeCD):
    valor = float(input('Digite o valor do CD: R$ '))
    media += valor

print(f'A quantidade CDs é {quantidadeCD}, o valor da coleção é R${media/quantidadeCD:.02f}')

