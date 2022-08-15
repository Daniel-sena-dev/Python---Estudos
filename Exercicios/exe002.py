def converterIdadeEmAnosParaDaias(ano):
    dias = 365 * ano
    return dias


ano = int(input('Digite sua idade: '))
dia = converterIdadeEmAnosParaDaias(ano)
print(f'Sua idade em dias é {dia}')