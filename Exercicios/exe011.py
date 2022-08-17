def remover(chave):
    del biblioteca[chave]


biblioteca = {
    'id': 20,
    'nome': 'caneta',
    'descricao': 'nao preenchido'
}
excluir = str(input('Digite qual chave voce deseja excluir: '))
remover(excluir)
print(biblioteca)
