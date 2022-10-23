"""A prefeitura de Vitória abriu uma linha de crédito para os funcionários. O valor máximo da
prestação não poderá ultrapassar 30% do salário bruto. Fazer um programa que
permita entrar com o salário bruto e o valor da prestação e informar se o empréstimo
pode ou não ser concedido.
"""

salario_Bruto = float(input("Informe o salário: "))
prestacao = float(input("Prestação: "))
if (salario_Bruto * 30/100) >= prestacao:
    print("Empréstimo pode ser concedido")
else:
    print("Empréstimo não pode ser concedido")
    