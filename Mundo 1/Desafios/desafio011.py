altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))
area = largura * altura
litroTinta = 2
pinta = area / litroTinta

print(f'A area da sua parede é de {area}m², você precisa de {pinta}L de tinta para pintar toda parede.')