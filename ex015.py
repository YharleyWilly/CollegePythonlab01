#Dadas 3 pontuações de finalistas em um campeonato, informe qual a pontuação que ficou em primeiro, segundo e terceiro lugar.

pont1 = int(input("Informe sua pontuação jogador 1: "))
pont2 = int(input("Informe sua pontuação jogador 2: "))
pont3 = int(input("Informe sua pontuação jogador 3: "))
if pont1 > pont2 > pont3:
    print("1º lugar Jogador 1 com Score:{}\n2º lugar Jogador 2 com Score:{}\n3º lugar Jogador 3 com Score:{}".format(pont1, pont2, pont3))
elif pont1 > pont3 > pont2:
    print("1º lugar Jogador 1 com Score:{}\n2º lugar Jogador 3 com Score:{}\n3º lugar Jogador 2 com Score:{}".format(pont1, pont3, pont2))
elif pont2 > pont1 > pont3:
    print("1º lugar Jogador 2 com Score:{}\n2º lugar Jogador 1 com Score:{}\n3º lugar Jogador 3 com Score:{}".format(pont2, pont1, pont3))
elif pont2 > pont3 > pont1:
    print("1º lugar Jogador 2 com Score:{}\n2º lugar Jogador 3 com Score:{}\n3º lugar Jogador 1 com Score:{}".format(pont2, pont3, pont1))
elif pont3 > pont1 > pont2:
    print("1º lugar Jogador 3 com Score:{}\n2º lugar Jogador 1 com Score:{}\n3º lugar Jogador 2 com Score:{}".format(pont3, pont1, pont2))
else:
    print("1º lugar Jogador 3 com Score:{}\n2º lugar Jogador 2 com Score:{}\n3º lugar Jogador 1 com Score:{}".format(pont3, pont2, pont1))