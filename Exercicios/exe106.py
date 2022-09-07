print('4- Programa para ler consoantes: ')
frase = str(input('Digite uma frase: ')).lower()
consoantes = 0

for cont in frase:
    if cont in 'qwrtypsdfghjklçzxcvbnm':
        consoantes += 1

print(f'Na frase {frase} tem {consoantes} consoantes.')
