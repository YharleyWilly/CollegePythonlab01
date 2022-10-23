""" Você irá fazer uma viagem internacional e precisa levar seu dinheiro em dólares. Elabore um
algoritmo para calcular e apresentar o valor da conversão de real (R$) para dólar (US$). O
algoritmo deverá solicitar o valor da cotação do dólar e quantos Reais(R$) você tem para
converter em dólar. Ao final mostre a quantidade de dólares que você irá levar para a viagem.
"""

cotacao = float(input("Informe quantos R$ (reais) valem $1 (dólar) neste momento: "))
real = float(input("Informe a quantia em R$ que deseja converter em dólar: "))
conversor = real/cotacao
print("Com R${:.2f} Real Brasileiro você irá levar para viagem ${:.2f} Dólar Americano: ".format(real, conversor))


