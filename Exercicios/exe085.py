print('33- coletar um numero inderterminado de temperaturas: ')
listaTemp = list()
media = 0


while True:
    try:
        temperatura = float(input('Digite uma temperatura (digite 999 para sair): '))
    except ValueError:
        print('ERRO! valor digitado invalido')
    else:
        if temperatura != 999:
            media += temperatura
            listaTemp.append(temperatura)
        else:
            break

print(f'Foi digitado um total de {len(listaTemp)}, é a media das temperaturas é {media/len(listaTemp):.02f}º')
