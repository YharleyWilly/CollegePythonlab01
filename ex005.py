'''
Muitos países estão passando a usar o sistema métrico. Preparar um algoritmo para executar
a conversão de Celsius para Fahrenheit.
A fórmula de conversão é: F= (9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a
temperatura em Celsius.
'''

c = float(input("Informe a temperatura em °C: "))
f = (9*c)+160
print("A temperatura de {}°C corresponde a {:.1f}°F".format(c, f))
