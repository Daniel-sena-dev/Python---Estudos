print('2- Programa para ler um nome de usuario e sua senha: ')


nomeUsuario = str(input('Digite um nome para usuario: '))
while True:
    try:
        senha = str(input('Digite uma senha (não digite o mesmo nome de usuario!): ')).strip()
    except ValueError:
        print('ERRO! Digite um valor valido')
    else:
        if senha == nomeUsuario or senha == '':
            print('Senha invalida')
        else:
            break

print(f'Cadastro realizado com sucesso! \nNome de usuario: {nomeUsuario}\nSenha: {senha}')
