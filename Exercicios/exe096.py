print('44- Votação eleitoral 2.0v: ')
saida = False
voto1 = voto2 = voto3 = voto4 = nulo = branco = totalVotos = 0

while True:
    if saida:
        break
    while True:
        try:
            voto = int(input('Digite seu voto: '))
        except ValueError:
            print('ERRO! valor invalido')
        else:
            if 1 <= voto <= 6:
                break
            elif voto == 0:
                saida = True
                break
            else:
                print('Valor invalido! ')

    if voto == 1:
        voto1 += 1
        totalVotos += 1
    elif voto == 2:
        voto2 += 1
        totalVotos += 1
    elif voto == 3:
        voto3 += 1
        totalVotos += 1
    elif voto == 4:
        voto4 += 1
        totalVotos += 1
    elif voto == 5:
        nulo += 1
        totalVotos += 1
    else:
        branco += 1
        totalVotos += 1

print(f'RESULTADOS:')
print(f'Total de votos no candidato 1: {voto1}')
print(f'Total de votos no candidato 2: {voto2}')
print(f'Total de votos no candidato 3: {voto3}')
print(f'Total de votos no candidato 4: {voto4}')
print(f'Total de votos no nulo: {nulo}')
print(f'Total de votos no branco: {(branco/totalVotos)*100:.02f}%')
print(f'Total percentual de votos nulos: {(nulo/totalVotos)*100:.02f}%')
