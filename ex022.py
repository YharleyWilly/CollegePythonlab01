'''Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das
seguintes categorias:
Infantil A = 5 a 7 anos
Infantil B = 8 a 11 anos
Juvenil A = 12 a 13 anos
Juvenil B = 14 a 17 anos
Adultos = Maiores de 18 anos
Menores que 5 anos não são classificados.
'''
idade = int(input("Informe sua idade: "))
if (5 <= idade <= 7):
    print("Categoria [Infantil A] = 5 a 7 anos")
elif (8 <= idade <= 11):
    print("Categoria [Infantil B] = 8 a 11 anos")
elif (12 <= idade <= 13):
    print("Categoria [Juvenil A] = 12 a 13 anos")
elif (14 <= idade <= 17):
    print("Categoria [Juvenil] B = 14 a 17 anos")
elif (idade > 18):
    print("Categoria [Adultos] = Maiores de 18 anos")
else:
    print("Categoria [Menores que 5 anos não são classificados]") 