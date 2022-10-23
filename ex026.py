""". Fazer um programa para entrar com um número inteiro e informar se ele é ou não
divisível por 3 e por 7.
"""

num = int(input("Digite um número: "))
if ((num % 3) == 0) and ((num % 7) == 0):
    print("{} é divisível por 3 e 7".format(num))
else:
    print("{} não é divisível por 3 e 7".format(num))