# o loop FOR serve para iterar os valores de uma coleção de um determinao numero de vezes
for letra in "Python":
    print(letra)

for numero in [1, 2, 3, 4, 5]:
    print(numero)

for i in range(1, 10, 2):
    print(f"numero: {i}")

sucesso = True
for numero in range(1, 4):
    print("a enviar", numero, numero * '-')
    if sucesso:
        print("O seu email foi enviado")
        break
else:
    print ("O Seu email nao foi enviado")

#loop for dentro de outro loop for

for i in range(1,5):
    for j in range(1, 4):
        print(f"i:{i}, j:{j}")

print()

#TABUADA
tabuada = 5
for tabuada in range(1,11):
    print(f"{tabuada} x {i} = {tabuada * i}")

#Tabuada do 1 ao 10

for i in range(1, 11):
    print()
    print(f"Tabuada do {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")