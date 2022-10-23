#Ler dois valores numéricos e apresentar a diferença do maior para o menor.
num1 = float(input("Digite um valor: "))
num2 = float(input("Digite o segundo: "))
if (num1 > num2):
    dif1 = num1 - num2
    print("Diferença entre {} e {}: {}".format(num1, num2, dif1))
else:
    dif2 = num2 - num1
    print("Diferença entre {} e {}: {}".format(num2, num1, dif2))
