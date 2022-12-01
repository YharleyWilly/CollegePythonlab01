estadoFiliais = []
filiaisPorEstado = []
faturamentoEstado = []
totalFaturamento = 0
totalFiliais = 0
aux = 0

print("---------------------------------------------- CADASTRO DE FILIAIS POR ESTADO ----------------------------------------------")

estado = int(input("\nQuantos estados você deseja cadastrar: "))

#Repetição para acrescentar estados na lista estadoFiliais

for c in range(estado):
   
    nomeEstado = input(f"Informe a sigla do {c+1}º estado: ").upper()
    estadoFiliais.append(nomeEstado)

print(f"\nEstados: {estadoFiliais}\n")

#Repetição para acrescentar quantidade de filiais por estado na lista filiaisPorEstado

for i in range(estado):
   
    quantFiliais = int(input(f"Informe a quantidade de filiais do estado {estadoFiliais[i]}: "))
    filiaisPorEstado.append(quantFiliais)

#Repetição para cálculo do total de filiais    

for f in filiaisPorEstado: 
    totalFiliais += f

print(f"\nQuantidade de filiais por estado: {filiaisPorEstado}")
print(f"Total de filiais: {totalFiliais}\n")

#Repetição para acrescentar faturamento de cada estado 

for e in range(estado):
    
    faturamento = float(input("Informe o faturamento do estado {} R$: ".format(estadoFiliais[e])))
    faturamentoEstado.append(faturamento)

#Cálculo faturamento total dos estados

for p in faturamentoEstado:
    totalFaturamento  += p

print(f"\nFaturamento por estado: {faturamentoEstado}")
print(f"Faturamento total R$: {totalFaturamento}")

#Menu para escolher o que fazer

menu = input("\n\n----------------------- Para acessar o MENU digite [menu] -- Para SAIR digite [sair] -----------------------\n\n").upper()

if menu == "MENU":
    
    while menu == "MENU":

        totalFaturamento=0
        totalFiliais=0

        escolha = int(input("\n------------- INSERIR DADOS - [1]   ALTERAR DADOS - [2]   REMOVER DADOS - [3]-----------\n\n"))
        
        if escolha == 1:
            aux += estado
            print("\n---------------- INSERIR NOVOS ESTADOS ----------------")
            estado = int(input("\nQuantos estados você deseja cadastrar: "))

            for a in range(estado):
                nomeEstado = input("Informe a sigla do estado: ").upper()
                estadoFiliais.append(nomeEstado)
            print(f"\nEstados: {estadoFiliais}")

            for i in range(estado):
                
                quantFiliais = int(input(f"Informe a quantidade de filiais do estado {estadoFiliais[aux+i]}: "))
                filiaisPorEstado.append(quantFiliais)

            #Repetição para cálculo do total de filiais    

            for f in filiaisPorEstado:
                totalFiliais += f

            print(f"\nQuantidade de filiais por estado: {filiaisPorEstado}")
            print(f"Total de filiais: {totalFiliais}\n")

            #Repetição para acrescentar faturamento de cada estado 

            for e in range(estado):
                faturamento = float(input("Informe o faturamento do estado {} R$: ".format(estadoFiliais[aux+e])))
                faturamentoEstado.append(faturamento)

            #Cálculo faturamento total dos estados

            for p in faturamentoEstado:
                totalFaturamento += p

            print(f"\nFaturamento por estado: {faturamentoEstado}")
            print(f"Faturamento total R$: {totalFaturamento}")
        

        if escolha == 2:
            print(f"\nESTADOS: {estadoFiliais}\nQUANTIDADE DE FILIAIS POR ESTADO: {filiaisPorEstado}\nFATURAMENTO POR ESTADO: {faturamentoEstado}")
            print("\n----------------------------------------------------------------- ALTERAR -----------------------------------------------------------------")

            escolhaAlterarDados = int(input("---------------- ESTADOS [1] ----- QUANTIDADE DE FILIAIS POR ESTADO [2] ----- FATURAMENTO POR ESTADO [3] ----------------\n\n"))
            
            if escolhaAlterarDados == 1:
                estadoAlterar= input("Qual estado deseja alterar: ").upper()
                #for i in range (estadoFiliais):
                for indice, valor in enumerate(estadoFiliais):
                    if estadoAlterar == valor:
                        estadoAlterar= input("Qual estado deseja inserir: ").upper()
                        estadoFiliais[indice] = estadoAlterar
                        print(estadoFiliais)
            
            if escolhaAlterarDados == 2 :
                estadoAlterar= input("Qual estado deseja alterar a quantidade de filiais: ").upper()
                for indice, valor in enumerate(estadoFiliais):
                    if estadoAlterar == valor:
                        estadoAlterar= int(input("Insira a nova quantidade de filiais: "))
                        filiaisPorEstado[indice] = estadoAlterar
                        print(filiaisPorEstado)

            if escolhaAlterarDados == 3 :
                estadoAlterar= input("Qual estado deseja alterar a quantidade de faturamento: ").upper()
                for indice, valor in enumerate(estadoFiliais):
                    if estadoAlterar == valor:
                        estadoAlterar= float(input("Insira o novo faturamento R$: "))
                        faturamentoEstado[indice] = estadoAlterar
                        print(faturamentoEstado)


        if escolha == 3 :
            
            print(f"\nESTADOS: {estadoFiliais}\nQUANTIDADE DE FILIAIS POR ESTADO: {filiaisPorEstado}\nFATURAMENTO POR ESTADO: {faturamentoEstado}")
            print("\n----------------------------------------------------------------- DELETAR -----------------------------------------------------------------")

            escolhaAlterarDados = int(input("---------------- ESTADOS [1] ----- QUANTIDADE DE FILIAIS POR ESTADO [2] ----- FATURAMENTO POR ESTADO [3] ----------------\n\n"))
            
            if escolhaAlterarDados == 1:
                estadoAlterar= input("Qual estado deseja deletar: ").upper()
                #for i in range (estadoFiliais):
                for indice, valor in enumerate(estadoFiliais):
                    if estadoAlterar == valor:
                        estadoFiliais[indice] = "#"
                        print(estadoFiliais)
            
            if escolhaAlterarDados == 2 :
                estadoAlterar= input("Qual estado deseja deletar a quantidade de filiais: ").upper()
                for indice, valor in enumerate(estadoFiliais):
                    if estadoAlterar == valor:
                        filiaisPorEstado[indice] = "#"
                        print(filiaisPorEstado)

            if escolhaAlterarDados == 3 :
                estadoAlterar= input("Qual estado deseja deletar a quantidade de faturamento: ").upper()
                for indice, valor in enumerate(estadoFiliais):
                    if estadoAlterar == valor:
                        faturamentoEstado[indice] = "#"
                        print(faturamentoEstado)
 
        menu = input("\n\n----------------------- Para acessar o MENU digite [menu] -- Para SAIR digite [sair] -----------------------\n\n").upper()
                        
elif menu == "SAIR":
    print("--------------------------------------------------------- FINISH ---------------------------------------------------------")
