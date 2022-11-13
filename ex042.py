"""

Faça um programa em Python que leia duas notas e a matrícula de 50 alunos, calcule e
imprima:

a) A média aritmética das notas de cada aluno e uma mensagem indicando se o aluno está
aprovado ou reprovado, conforme quadro abaixo:

Média Aritmética                        Mensagem
Menor ou igual 5,0      Aluno com matrícula xxxx está reprovado
Maior do que 5,0        Aluno com matrícula xxxx está aprovado

b) O total de alunos aprovados;
c) O total de alunos reprovados;
d) A média aritmética da turma.

"""

totalAprovados = 0
totalReprovados = 0
somaNotas = 0

for c in range(1, 3):

    matricula = int(input("Digite sua matrícula: "))
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    somaNotas = (nota1 + nota2) + somaNotas
    media = (nota1 + nota2) / 2

    print(f"A média do aluno corresponde a: {media}")

    if media <= 5:
        totalReprovados += 1
        print(f"Aluno com matrícula {matricula} está reprovado")
    else:   
        totalAprovados += 1
        print(f"Aluno com matrícula {matricula} está aprovado")
    
mediaTurma = somaNotas / c

print(f"A média aritmética da turma é {mediaTurma}")