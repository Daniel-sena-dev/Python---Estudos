nome = input('Digite seu nome completo: ')
nomeDividido = nome.split()
tamanhoLista= len(nomeDividido)

print(tamanhoLista)
print(f'Primeiro nome: {nomeDividido[0]}')
print(f'Ultimo nome: {nomeDividido[tamanhoLista-1]}')
