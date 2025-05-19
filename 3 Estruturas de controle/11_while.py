
contar = 0
while contar < 5:
    print(contar)
    # contar = contar + 1
    contar += 1

i = 0
while True:
    i += 1
    if i == 7:
        break
    print(i)

print()

# A Função imput permite ao utilizador inserir
username = input("Insira um username: ")
print(f"O Seu username {username} foi validado, pode entrar no site")

nome = input(" Insira o seu nome: ")
idade = input(" Insira a sua idade: ")
if idade >= 10:
    print(f"Olá {nome}, Bem vindo ao python. Como ja tens {idade} anos, já podes aprender a programar")
else:
    print(f"Olá {nome}, ainda só tens {idade} anos, tens que esperar até teres 10")

# Loop while com input
print("Bem vindo ao programa \"Multiplica por 2\"")
print(" Insira um numero que será multiplicado por 2")

opcao =""
while opcao != "s":
    numero = int(input("Insira um numero: "))
    print(f"O numero {numero} multiplicado por 2 é {numero * 2}")
    opcao = input("Quer terminar o programar? (s para sair, enter para continuar)").lower()

