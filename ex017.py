"""Faça um algoritmo onde deverá ser informado um número. O algoritmo deverá exibir se o
número é positivo, negativo ou nulo.
"""
num = float(input("Digite um número: "))
if (num >= 1):
    print("{} é positivo!".format(num))
elif (num <= -1):
    print("{} é negativo!".format(num))
elif (num == 0):
    print("{} é nulo!".format(num))
else:
    print("Digite um número.")

