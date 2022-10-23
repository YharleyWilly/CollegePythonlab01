#Faça um programa para ler 2 números inteiros, e apresente o quociente e o resto da divisão
#entre eles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))
quociente = n1//n2
resto = n1%n2
print("Quociente entre {} e {}: {}\nResto da divisão entre {} e {}: {}".format(n1, n2, quociente, n1, n2, resto))
