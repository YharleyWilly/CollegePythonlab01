"""
Inicializar as variáveis FATORIAL e CONTADOR com 1; Solicitar o valor de um número para
calcular a seu fatorial; Multiplicar sucessivamente a variável FATORIAL pela variável
CONTADOR; Incrementar 1 à variável CONTADOR, efetuando o controle até o valor solicitado;
Apresentar ao final o valor obtido.
"""

n = int(input("Digite um número para calcular seu fatorial: "))
cont = n
fatorial = 1
print(f"{n}! =", end = " ")
for controlador in range(n, 0, -1):
    fatorial = fatorial * cont
    cont = cont - 1
    print(f"{controlador}", end = " ")
    if controlador != 1:
        print("x", end = " ")
    else:
        print(f"= {fatorial}", end = " ")
        


    




    

    