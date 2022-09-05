print('43- Cardapio 1.0v')
quantidade = codigo = total = 0
saida = False

print('=-=' * 15)
print(f'{"Especificação       Código         Preço"}'.center(30))
print('=-=' * 15)
print(f'Cachorro Quente        100         R$ 1,20'.center(30))
print(f'Bauru Simples          101         R$ 1,30'.center(30))
print(f'Bauru com ovo          102         R$ 1,50'.center(30))
print(f'Hambúrguer             103         R$ 1,20'.center(30))
print(f'Cheeseburguer          104         R$ 1,30'.center(30))
print(f'Refrigerante           105         R$ 1,00'.center(30))

while True:
    if saida:
        break

    while True:
        try:
            codigo = int(input('Digite o codigo do lanche: '))
        except ValueError:
            print('Erro! Digite um valor valido')
        else:
            if codigo == 100 or codigo == 101 or codigo == 102 or codigo == 103 or codigo == 104 or codigo == 105:
                break
            else:
                print('Valor invalido!')

    quantidade = int(input('Digite a quantidade que você deseja: '))

    if codigo == 100:
        total += 1.20 * quantidade
    elif codigo == 101:
        total += 1.30 * quantidade
    elif codigo == 102:
        total += 1.50 * quantidade
    elif codigo == 103:
        total += 1.20 * quantidade
    elif codigo == 104:
        total += 1.30 * quantidade
    elif codigo == 105:
        total += 1.00 * quantidade

    while True:
        sair = input('Desejar finalizar o pedido [S/N]: ').upper()[0]
        if sair == 'S':
            saida = True
            break
        else:
            break

print(f'O total da conta foi R${total:.02f}')
