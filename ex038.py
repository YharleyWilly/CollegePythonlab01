"""

Escrever um algoritmo que leia um conjunto de valores e calcule a média aritmética dos
valores lidos, a quantidade de valores positivos e o percentual de valores negativos. Mostre os
resultados no final. Para terminar o programa, o usuário deverá digitar o valor zero. O valor
zero não entra nos cálculos.

"""

positivos = 0
percNegativos = 0
contador = 0
soma = 0
c = int(input("Digite um valor ou 0 para sair: "))
while (c != 0):
    soma += c
    contador += 1
    if (c > 0):
        positivos += 1
    c = int(input("Digite um valor ou 0 para sair: ")) 
media = soma / contador
print(f"A soma dos valores = {soma}")
print(f"A média dos valores = {media}")
print(f"O percentual de números negativos é {((contador - positivos) * 100) / contador} %")
