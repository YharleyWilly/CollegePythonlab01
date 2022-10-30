""" 
Faça um programa que escreve na tela a mesma frase 10 vezes. E depois faça com que o
programa mostre o número de cada linha no início e no final da linha, conforme exemplo:

1 Sou um programa Python! 1
2 Sou um programa Python! 2
3 Sou um programa Python! 3
"""

#Utilizando "For"

frase = input("Digite uma frase: ")
for cont in range(1, 11):
    print(f"{cont} {frase} {cont}")

#Utilizando "While"

frase = input("Digite uma frase: ")
cont = 0
while cont < 10:
    cont = cont + 1
    print(f"{cont} {frase}! {cont}")


