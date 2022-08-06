#DICIONARIO
locadora = []

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'}
filme2 = {
    'titulo': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'}
filme3 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'}

locadora.append(filme)
locadora.append(filme2)
locadora.append(filme3)

print(locadora[0]['ano'])
print(locadora[0]['titulo'])
print(locadora[0]['diretor'])

