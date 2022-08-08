def notas(*alunoNotas, sit=True):
    """
    :param alunoNotas: notas dos alunos
    :param sit: mostrar ou nao a situação da turma [Boa/Razoavel/Ruim]
    :return: retorna um dicionario com informações da turma
    """
    totalNotas = media = 0
    situacao = ''
    maiorNota = max(alunoNotas)
    menorNota = min(alunoNotas)
    for contador in range(0, len(alunoNotas)):
        totalNotas += alunoNotas[contador]
    media = totalNotas/len(alunoNotas)
    #Criando dic
    situAluno = dict()
    situAluno['total'] = len(alunoNotas)
    situAluno['maior'] = maiorNota
    situAluno['menor'] = menorNota
    situAluno['média'] = media
    if sit:
        if media >= 7:
            situacao = 'BOA'
        elif media >= 5:
            situacao = 'RAZOAVEL'
        else:
            situacao = 'RUIM'
        situAluno['situação'] = situacao
    return situAluno


# Programa principal:
resp = notas(6, 6, 6, sit=True)
print(resp)
