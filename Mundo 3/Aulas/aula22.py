# Erros e exceções
try:
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))
    resto = numerador / denominador
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(('Não é possível dividir um número por zero!'))
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro foi {erro.__cause__}')
else:
    print(f'O resultado é {resto}')
finally:
    print('Volte sempre! Muito obrigado!')
