"""Faça um algoritmo onde deverá ser informado nome, nota de trabalho e nota da prova. O
algoritmo deverá calcular a média e se a média for maior que 7(sete), imprimir o nome do
aluno e a situação “aprovado”, senão “reprovado”.
"""
name = input("Informe seu nome: ")
nota = float(input("Informe a nota do trabalho: "))
notaProva = float(input("Informe a nota da prova: "))
media = (nota+notaProva)/2
if (media > 7):
    print("{}: APROVADO".format(name))
else:
    print("{}: REPROVADO".format(name))