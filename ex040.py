"""

Suponha que para cada tipo de computador fabricado, a SEI (empresa de Tecnologia), tem
as seguintes informações:
- Nome do computador;
- Nome do fabricante;
- Capacidade de armazenamento do computador;
Faça um algoritmo que leia os dados acima (considere –1 fim de entrada de dados) e que:
a) Determine qual o valor da maior capacidade de memória;
b) Determine quantos computadores diferentes a Intel fabrica;
c) Verifique se tem algum computador chamado i7. Se tiver, qual o seu fabricante.

"""

intelFabrica = 0
maiorMemoria = 0
computadorNomeFabricante = ""

nomeComputador = input("Nome do computador ou -1 para sair: ")
while nomeComputador != "-1":
    
    nomeFabricante = input("Nome do fabricante: ").upper()

    if nomeComputador == "i7":
        print(f"Existe um computador i7, seu fabricante é {nomeFabricante}")

    armazenamentoComputador = float(input("Armazenamento do computador: "))
    if armazenamentoComputador > maiorMemoria:
        maiorMemoria = armazenamentoComputador
        computadorMaiorMemoria = nomeComputador
        computadorNomeFabricante = nomeFabricante

    nomeComputador = input("Nome do computador ou -1 para sair: ")

    if nomeFabricante == "INTEL":
        intelFabrica += 1
    
print(f"O computador {computadorMaiorMemoria} possui o maior armazenamento: {maiorMemoria}")    
print(f"A Intel fabrica: {intelFabrica} computadores diferentes")
