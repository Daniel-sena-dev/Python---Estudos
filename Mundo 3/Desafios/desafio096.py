def area(largura, comprimento):
    A = largura * comprimento
    print(f'A area do terro com largura {largura} e comprimento {comprimento} e {A:.02f}m².')

print('Controle de Terrenos')
print('-' * 20)
area(float(input('LARGURA(m): ')), float(input('COMPRIMENTO(m): ')))
