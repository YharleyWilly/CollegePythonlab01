""" Crie um algoritmo que efetue o cálculo do salário líquido de um professor. Serão
fornecidos: valor da hora aula, o número de aulas dadas no mês e percentual de
desconto no INSS. Se o professor ganhar mais que 10 salários mínimos dizer que
“Sortudo!”, se ele receber entre 6 e 9 salários mínimos, exibir a seguinte mensagem: “Um
dia você chega lá!”, se receber menos que 6 salários mínimos você deverá exibir a
seguinte mensagem: “Ah! Coitado!”.
"""
valorHora = float(input("Informe o valor da hora aula (R$#####.##): R$"))
horasAula = float(input("Informe quantas horas são trabalhadas no dia: "))
aulasMes = int(input("Informe número de aulas dadas no mês: "))
descInss = float(input("Informe percentual de desconto no INSS (###.##%): "))
salarioLiquido = ((valorHora * horasAula) * aulasMes) * (descInss/100)
if (salarioLiquido > 9900):
    print("SORTUDO!")
    print("R$",salarioLiquido)
elif (6600 <= salarioLiquido <= 9900):
    print("UM DIA VOCÊ CHEGA LÁ!")
    print("R$",salarioLiquido)
else:
    print("AH! COITADO!")
    print("R$",salarioLiquido)

