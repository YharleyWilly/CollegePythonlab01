"""

Dados dois números inteiros A e B, construa um algoritmo para calcular a soma de todos os
inteiros existentes entre A e B.

"""

contador = 1
soma = 0
a = int(input("Digite um número inteiro para A: "))
b = int(input("Digite um número inteiro para B: "))
if a < b:
    for c in range(a, b-1):
        contador = contador + 1
        soma = soma + contador
    print(f"Entre {a} e {b} existem {c} números")
    print(f"A soma de todos os números entre {a} e {b} é igual a {soma}")
elif a > b:
    contador = 1
    soma = 0
    for c in range(b, a-1):
        contador = contador + 1
        soma = soma + contador
    print(f"Entre {a} e {b} existem {c} números")
    print(f"A soma de todos os números entre {a} e {b} é igual a {soma}")
    
    











