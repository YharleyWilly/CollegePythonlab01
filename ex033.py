"""

Faça um programa que vai pedindo números ao usuário até que este introduza o número -1.
O computador deve dizer a média dos números introduzidos (excluindo o -1).

"""

contador = 0
soma = 0
n = float(input("Digite um número ou -1 para sair: "))
while (n != -1):
    n = float(input("Digite um número: "))
    if (n == -1):
        break
    soma += n
    contador += 1
    media = soma / contador
print(media)






