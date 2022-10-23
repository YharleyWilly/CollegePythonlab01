#Construir um algoritmo para ler 3 valores reais, calcular e imprimir a média desses valores.

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
media = (n1+n2+n3)/3
print("A média desses valores é igual a: {:.2f}".format(media))
