print('21- Programa caixa eletronico 1.0v')
dinheiro = int(input('Digite um valor de 10 até 600: '))
dinheiroCopy = dinheiro
nota100 = nota50 = nota10 = nota5 = nota1 = 0

if 0 < dinheiro <= 600:
    if dinheiro // 100:
        nota100 = dinheiro // 100
        dinheiro = dinheiro % 100
    if dinheiro // 50:
        nota50 = dinheiro // 50
        dinheiro = dinheiro % 50
    if dinheiro // 10:
        nota10 = dinheiro // 10
        dinheiro = dinheiro % 10
    if dinheiro // 5:
        nota5 = dinheiro // 5
        dinheiro = dinheiro % 5
    if dinheiro // 1:
        nota1 = dinheiro // 1
    print(f'O saque foi liberado!')
    print(f'O valor pedido foi de {dinheiroCopy}')
    print(f'Serão {nota100} de 100')
    print(f'Serão {nota50} de 50')
    print(f'Serão {nota10} de 10')
    print(f'Serão {nota5} de 5')
    print(f'Serão {nota1} de 1')
