print('26- programa eleitoral 1.0v: ')
quantidadeEleitores = int(input('Digite a quantiddade de eleitores: '))
candidato1 = 0
candidato2 = 0
candidato3 = 0
nulo = 0

for cont in range(0, quantidadeEleitores):
    while True:
        try:
            voto = int(input('[1] - Candidato 1\n[2] - Candidato 2\n[3] - Candidato 3\nDigite seu voto: '))
        except ValueError:
            print(f'Erro! numero digitado invalido')
        else:
            if voto == 1:
                candidato1 += 1
                break
            elif voto == 2:
                candidato2 += 1
                break
            elif voto == 3:
                candidato3 += 1
                break
            else:
                nulo = 0
                break

print('RESULTADO:')
print(f'Candidato 1: {candidato1}')
print(f'Candidato 2: {candidato2}')
print(f'Candidato 3: {candidato3}')
print(f'Nulos: {nulo}')
