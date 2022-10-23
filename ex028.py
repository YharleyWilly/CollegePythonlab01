""" Faça um programa que receba o valor do salário de uma pessoa e o valor de um
financiamento pretendido. Caso o financiamento seja menor ou igual a 5 vezes o
salário da pessoa, o programa deverá escrever "Financiamento Concedido"; senão,
escreverá "Financiamento Negado". Independente de conceder ou não o
financiamento, o programa escreverá depois a frase "Obrigado por nos consultar."
"""

salario = float(input("Informe seu salário: R$"))
financiamento = float(input("Financiamento pretendido: R$"))
if (financiamento < salario) or (financiamento == (salario * 5)):
    print("FINANCIAMENTO CONCEDIDO")
    print("Obrigado por nos consultar")
else:
    print("FINANCIAMENTO NEGADO")
    print("Obrigado por nos consultar")

