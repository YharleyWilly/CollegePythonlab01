#Faça um algoritmo para somar os restos da divisão por 3 de 200 números inteiros.

soma = 0
for c in range(1, 201):
    resto = c % 3
    soma += resto
print(soma)

