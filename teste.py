emprestimo = int(input('Qual o valor do Emprestimo:R$ '))
parcelas = int(input('Quantas parcelas: '))
juros = (emprestimo * 20) / 100
print(f'Com o valor do Empréstimo sendo R${emprestimo} o juros vai ficar R${juros:.2f} de Juros')
print(f'Vai ficar {parcelas} parcelas de R${(emprestimo+juros)/parcelas:.2f}!')
