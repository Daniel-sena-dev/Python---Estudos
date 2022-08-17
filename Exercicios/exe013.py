def objetoParaArray(bibli):
    listaGeral = list()
    listaInterna = list()
    for chaves, valores in bibli.items():
        listaInterna.append(chaves)
        listaInterna.append(valores)
        listaGeral.append(listaInterna[:])
        listaInterna.clear()
    return listaGeral


biblioteca = {
    'nome': 'Daniel',
    'profissao': 'desenvolvedora de software'
}

saida = objetoParaArray(biblioteca)
print(saida)
