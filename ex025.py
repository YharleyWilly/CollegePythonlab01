"""Faça um algoritmo que receba três valores que representarão os lados de um triângulo e
serão fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique
esse triângulo como:

equilátero – três lados iguais;
isósceles – dois lados iguais;
escaleno – três lados diferentes.

Lembre-se de que, para formar um triângulo:

• Nenhum dos lados pode ser igual a zero;
• Um lado não pode ser maior do que a soma dos outros dois.
"""

l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
if ((l2 - l3) < l1 < (l2 + l3)) and ((l1 - l3) < l2 < (l1 + l3)) and ((l1 - l2) < l3 < (l1 + l2)) and (l1 == l2 == l3):
    print("Triângulo equilátero - três lados iguais")
elif ((l2 - l3) < l1 < (l2 + l3)) and ((l1 - l3) < l2 < (l1 + l3)) and ((l1 - l2) < l3 < (l1 + l2)) and (l1 == l2) and (l2 != l3) or (l1 == l3) and (l2 != l3) or (l3 == l1) and (l2 != l1) or (l3 == l2) and (l1 != l2):
    print("Triângulo isósceles - dois lados iguais")
elif ((l2 - l3) < l1 < (l2 + l3)) and ((l1 - l3) < l2 < (l1 + l3)) and ((l1 - l2) < l3 < (l1 + l2)) and (l1 != l2 != l3) and (l1 != l3):
    print("Triângulo escaleno = três lados diferentes") 
else:
    print("Os valores dos lados não formam um triângulo")
