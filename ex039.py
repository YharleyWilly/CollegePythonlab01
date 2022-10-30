"""

Os regulamentos de pesca do Estado de São Paulo impõem um limite no peso total de pesca de um
dia. Suponha que você planeje levar seu terminal portátil de computador em sua próxima pescaria e
deseje um programa para calcular quanto você excedeu seu limite. 

Preparar um algoritmo que leia o limite diário (em quilogramas) e, então, leia os valores de entrada um por um (os pesos dos peixes à
medida que são apanhados) e imprima uma mensagem no ponto quando este limite é excedido. Um peso
de zero indica o fim de entrada. Após o registro de cada peixe, o algoritmo deve imprimir o peso total de
peixes obtidos até aquele ponto.

"""

pesoPeixe, totalPeso = 0, 0
limiteDia = float(input("Qual o limite de kg de pescaria neste dia?"))
pesoPeixe = float(input("Digite o peso do peixe ou zero para finalizar a pescaria:"))
while pesoPeixe != 0:
    totalPeso = totalPeso + pesoPeixe
    print("O total de peso até o momento é " + str(totalPeso))
    if totalPeso > limiteDia:
        print("O limite diário foi excedido.")
    pesoPeixe = float(input("Digite o peso do peixe ou zero para finalizar a pescaria:"))

    

