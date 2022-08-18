print('12- Programa para calcular o peso ideal')
altura = float(input('Digite sua altura: '))
pesoIdeal = (72.7 * altura) - 58
print(f'Seu peso ideal é {pesoIdeal:.02f}Kg')
print('-' * 40)

print('13- Programa para calcular o peso ideal de M/F:')
altura = float(input('Digite sua altura: '))
print(f'A) peso ideal para homens: ')
pesoIdeal = (72.7 * altura) - 58
print(f'Seu peso ideal é {pesoIdeal:.02f}Kg')
print(f'B) peso ideal para mulheres: ')
pesoIdeal = (62.1 * altura) - 44.7
print(f'Seu peso ideal é {pesoIdeal:.02f}Kg')
print('-' * 40)

print('14- Programa para rendimento de trabalho: ')
pesoPeixes = float(input('Digite o peso dos peixes pescados: '))
excesso = pesoPeixes - 50
multa = 4 * excesso
print(f'A quantidade de peixes pescados foram de: {pesoPeixes}Kg, o excedente de {excesso}Kg e a multa aplicada é de R${multa:.02f}')
