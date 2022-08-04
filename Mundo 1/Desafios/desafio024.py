cidade = input('Que cidade você mora? ')
nomeCidade = cidade.lower().split()
print(nomeCidade[0].find('santo'))
print("O nome da sua cidade começa com SANTO" if nomeCidade[0] == 'santo' else "Não começa com SANTO")


