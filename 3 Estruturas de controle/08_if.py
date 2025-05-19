#Operadores
# == igual a
# != diferente de
# > maior que
# >= maior ou igual que
# < menor que
# <= menor ou igual que

#condição if simples
idade= 18
if idade >= 18:
    print("Já é maior de idade")
else:
    print("Ainda é menor de idade")

#condição if else
idade= 17
if idade >= 18:
    print("Já é maior de idade")
else:
    print("Ainda é menor de idade")

#condição com if elif e else
idade= 17
if idade >= 18:
    print("Já é adulto, preço do bilhete é 15 euros")
elif idade >= 14:
    print("É adolescente, o preço do bilhete são 10 euros")
else:
    print("É Criança, o preço do bilhe são 5 euros")

#Utilizar if com 2 condições
idade = 22
tem_carta = True

if idade >=18 and tem_carta:
    print ("Já é adulto e tem carta, pode conduzir")
elif idade >= 18:
    print("Já é adulto mas nao tem carta")
else:
    print(" Ainda nao tem idade para conduzir")

#Com a palavra 'or' apenas uma das condições precisa de ser verdadeira
condutor ="Pesados"
if condutor == "Pesados" or condutor == "Ligeiros":
    print("O Condutor pode conduzir veiculos")
elif condutor != "Pesados" or condutor == "Ligeiros":
    print ("O Conduto pode conduzir veiculos")
else: 
    print("Você nao pode conduzir veiculos")