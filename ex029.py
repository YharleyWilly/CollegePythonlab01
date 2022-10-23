""" Leia uma média e um número de faltas dadas a um aluno e imprima aprovado, reprovado
por média e por falta, reprovado por média ou reprovado por falta. Sendo média maior
igual a 7 indica aprovado, e faltas maior igual a 32 indica reprovado.
"""

media = float(input("Informe a média: "))
faltas = int(input("Número de faltas: "))
if (media >= 7) and (faltas >= 32):
    print("REPROVADO POR FALTA")
elif (media < 7) and (faltas >= 32):
    print("REPROVADO POR MÉDIA E FALTA")
elif (media < 7):
    print("REPROVADO POR MÉDIA")
else:
    print("APROVADO")