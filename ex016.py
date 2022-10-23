#Ler 2 números inteiros do teclado (A e B), verificar e imprimir qual deles é o maior, ou a mensagem “A=B” caso sejam iguais.
a = int(input("Digite um número: "))
b = int(input("Digite mais um número: "))
if (a > b):
    print("{} é maior que {}".format(a, b))
elif (a < b):
    print("{} é maior que {}".format(b, a))
else:
    print(a,"=",b)