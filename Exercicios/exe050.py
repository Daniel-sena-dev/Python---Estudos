print('26- Programa para posto: ')
tipoCombustivel = str(input('Digite qual combustivel voce vai abastecer: Gasolina ou Alcool: ')).upper()[0]
litros = float(input('Digite a quantidade de litros que você deseja abastacer: '))
valorTotal = desconto = 0

if tipoCombustivel == 'A':
    if litros <= 20:
        valorTotal = litros * 1.9
        desconto = valorTotal * 0.03
        valorTotal = valorTotal - desconto
    else:
        valorTotal = litros * 1.9
        desconto = valorTotal * 0.05
        valorTotal = valorTotal - desconto
elif tipoCombustivel == 'G':
    if litros <= 20:
        valorTotal = litros * 2.5
        desconto = valorTotal * 0.04
        valorTotal = valorTotal - desconto
        print(f'O combustível colocado foi {tipoCombustivel}, o valor total com desconto foi de R${valorTotal:.02f}')
    else:
        valorTotal = litros * 2.5
        desconto = valorTotal * 0.06
        valorTotal = valorTotal - desconto
        print(f'O combustível colocado foi {tipoCombustivel}, o valor total com desconto foi de R${valorTotal:.02f}')
else:
    print('Tipo do combustivel invalido!')
