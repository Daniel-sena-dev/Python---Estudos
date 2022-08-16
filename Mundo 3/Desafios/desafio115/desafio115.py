from lib.interface import *
from lib.arquivo import *
import time

arq = 'dadospessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31mERRO! digite uma opção valida\033[m')
    time.sleep(2)
