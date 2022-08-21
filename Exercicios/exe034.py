print('10- programa para dar saudações')
turno = str(input('Digite o turno que você estuda [Matutino/Vespertino/Noturno]: ')).lower()[0]
if turno == 'm':
    print('Bom Dia!')
elif turno == 'v':
    print('Boa Tarde!')
else:
    print('Boa Noite!')
