'''
Escreva um algoritmo para determinar o consumo médio de um automóvel sendo que será
fornecida via teclado a distância total percorrida pelo automóvel e o total de combustível gasto.
'''

km = float(input("Informe a distancia total percorrida pelo automóvel em quilômetros: "))
cb = float(input("Informe o combustível gasto em litros: "))
consumomedio = km/cb
print("O consumo médio do automóvel é de: {:.2f}km/l ".format(consumomedio))
