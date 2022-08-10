from pacotesModulos.moeda import resumo
from pacotesModulos.dado import validacao

preco = validacao('Digite o preco: R$')
resumo(preco, 80, 35)
