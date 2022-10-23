"""Leia o valor do salário atual de um funcionário e calcule o reajuste salarial conforme
percentual abaixo:
salário < 500, reajuste de 15%
salário >= 500 e <= 1000, reajuste de 10%
salário > 1000, reajuste de 5%
Ao final, apresente o valor do novo salário.
"""

salario = float(input("Informe seu salário atual (R$:#####.##) R$: "))
reaj15 = 1.15 * salario
reaj10 = 1.10 * salario
reaj5 = 1.05 * salario
if (salario < 500):
    print("Com o reajuste salarial de 15% o salário passa a ser R$: {:.2f}".format(reaj15))
elif (500 <= salario <= 1000):
    print("Com o reajuste salarial de 10% o salário passa a ser R$: {:.2f}".format(reaj10))
else:
    print("Com o reajuste salarial de 5% o salário passa a ser R$: {:.2f}".format(reaj5))

