"""

Construir um algoritmo para gerar a seguinte série:

s = 1/1 + 1/2 + 1/3 + ... + 1/n para os 50 primeiros termos.

"""

soma = 0
contador = 0
for c in range(1, 51):
    contador += 1
    soma += 1/contador
print(soma)