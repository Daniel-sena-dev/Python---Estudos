def voto(anoNascimento):
    import datetime
    anoAtual = datetime.date.today().year
    idade = anoAtual - anoNascimento
    if 18 <= idade <= 64:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO '
    elif idade >= 16 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


nascimento = int(input('Ano nascimento: '))
saida = voto(nascimento)
print(saida)
