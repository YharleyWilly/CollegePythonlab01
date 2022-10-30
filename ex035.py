"""

Faça um algoritmo que leia a altura de moças inscritas em um concurso de beleza. Para
finalizar será digitado zero na altura. Imprima a maior altura digitada.

"""
maiorAltura = 1
altura = 1
while (altura > 0):
    altura = float(input("Informe sua altura ou aperte [0] para finalizar: "))
    if (maiorAltura == 1 and altura <= 0):
        print("Valor inválido")
        continue
    if altura > maiorAltura:
        maiorAltura = altura
if (altura >= 0 and maiorAltura >= 0):       
    print("A maior altura digitada foi de {:.2f}".format(maiorAltura))