#Crie um programa onde você define o objetivo que ele tem que executar.
""" Programa que facilita o trabalho de um pintor, ajudando ele dizendo o quanto de tinta será necessário
para pintar uma parede. Programa pergunta a largura e comprimento da parede, calcula a área da parede, per
gunta quantos litros de tinta são necessários para pintar 2 metros², pergunta quantos litros de tinta 
o usuário do programa possui.

"""

larg = float(input("Informe a largura da parede: "))
comp = float(input("Informe o comprimento da parede: "))
area = larg*comp
lt_tinta = float(input("Quantos litros de tinta pintam 2m²: "))
parede = (lt_tinta*area)/2
print("Para pintar a parede de {:.2f}x{:.2f} serão necessários {:.2f}l de tinta".format(larg, comp, parede))

