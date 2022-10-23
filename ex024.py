""" Um endocrinologista deseja controlar a saúde de seus pacientes, e para isso, se utiliza o
índice de massa corporal (IMC). Sabendo que o IMC é calculado através da fórmula
IMC=peso/altura², crie um algoritmo que apresente o nome do paciente e a faixa de risco,
baseando na seguinte tabela:

           IMC         |           Faixa de Risco

Abaixo dos 20          | Abaixo do peso
A partir dos 20 até 25 | Normal
A partir dos 25 até 35 | Excesso de peso
A partir dos 35 até 50 | Obesidade
A partir dos 50        | Obesidade Mórbida

"""
nome = input("Qual o seu nome? ")
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso/(altura**2)
if (imc < 20):
       print("{}. Faixa de risco: Abaixo do peso".format(nome))
elif (20 <= imc <= 25):
       print("{}. Faixa de risco: Normal".format(nome))
elif (25 <= imc <= 35):
       print("{}. Faixa de risco: Excesso de peso".format(nome))
elif (35 <= imc <= 50):
       print("{}. Faixa de risco: Obesidade".format(nome))
else: 
       print("{}. Faixa de risco: Obesidade Mórbita".format(nome))
