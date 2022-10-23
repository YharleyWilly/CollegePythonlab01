"""Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar ao final do programa o seu nome, o salário fixo e salário
no final do mês.
"""

nome = input("Qual é o seu nome?: ")
salario = float(input("Informe seu salario fixo R$: "))
total_vendas = float(input("Informe o total de vendas efetuadas por mês em dinheiro R$: "))
comissao = total_vendas*0.15
print(nome)
print("{:.2f}".format(salario))
print("Salário no final do mês: {:.2f}".format(salario+comissao))




