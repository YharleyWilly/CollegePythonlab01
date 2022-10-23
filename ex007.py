'''
Faça um programa para calcular e apresentar o volume de uma lata de óleo, utilizando a
fórmula volume = 3.14159 ∗ raio ∗ raio ∗ altura. Identifique na fórmula os valores de entrada de
dados e leia-os via teclado.
''' 
raio = float(input("Digite o raio da lata de óleo: "))
altura = float(input("Digite a altura da lata de óleo: "))
volume = 3.14159 * (raio**2) * altura
print("O volume da lata de óleo corresponde a: {:.2f}".format(volume))

