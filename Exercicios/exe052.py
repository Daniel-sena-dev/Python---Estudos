print('28- Prograpa para hipermercado tabajara 2.0v')
carnes = ['Filé Duplo', 'Alcatra', 'Picanha']
tipoCarne = int(input('File Duplo [0] \nAlcatra [1] \nPicanha [2] \nDigite qual carne você deseja: '))
KG = float(input('Quantos Kg você deseja? '))
cliente = str(input('Você tem nosso cartão? Sim ou Não')).upper()[0]
valorTotal = desconto = 0

if tipoCarne == 0:
    if KG <= 5:
        valorTotal = 4.9 * KG
        if cliente == 'S':
            desconto = valorTotal * 0.05
    else:
        valorTotal = 5.8 * KG
        if cliente == 'S':
            desconto = valorTotal * 0.05
elif tipoCarne == 1:
    if KG <= 5:
        valorTotal = 5.9 * KG
        if cliente == 'S':
            desconto = valorTotal * 0.05
    else:
        valorTotal = 6.8 * KG
        if cliente == 'S':
            desconto = valorTotal * 0.05
elif tipoCarne == 2:
    if KG <= 5:
        valorTotal = 6.9 * KG
        if cliente == 'S':
            desconto = valorTotal * 0.05
    else:
        valorTotal = 7.8 * KG
        if cliente == 'S':
            desconto = valorTotal * 0.05
else:
    print('Valor da carne invalida!')

print('-' * 10)
print('CUPOM FISCAL')
print('-' * 10)
print(f'Tipo da carne: {carnes[tipoCarne]}')
print(f'Quantidade da carne: {KG}')
print(f'Preço total: R${valorTotal:.02f}')
print(f'Desconto: R${desconto:.02f}')
print(f'Valor final: R${valorTotal - desconto:.02f}')
