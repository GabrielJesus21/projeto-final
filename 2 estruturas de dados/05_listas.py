lista = []
print(type(lista))

# Lista de elementos
marcas = ["Audi", "Peugeot", "Ferrari"]
print(f"O meu carro de sonho é o {marcas[2]}")

# Tamanha de uma lista
print(len(marcas))

# Adicionar um elemento à lista
marcas.append("bmw")
print(marcas[-1].upper())

# Remover um elemento da lista
marcas.remove("Peugeot")
print(marcas)

# Diferentes elementos numa lista
dados_carros = ["Audi", 2024, 30.120, True]

motos = ["suzuki", "honda", "kawasaki", "ducati"]

#Alterar elemento de uma lista
motos[0] = "harley"

# inserir elemento com base no seu índice
motos.insert(0, "ktm")

# Remover um elemento da lista
motos.remove("ktm")
motos.pop(2)

print(motos)

revertida =  motos[::-1]
print(revertida)

# Ordenar lista 
ordenados = motos.sort()
print(ordenados)

# Juntar elementos da lista como uma string
print(" - l ".join(motos))

#Exercicios 
# 1 - Crie uma lista com os nomes dos três jogos preferidos e imprima-os individualmente

jogos = ["Cs", "Fortnite", "Fifa"]
print(jogos[0])
print(jogos[1])
print(jogos[2])

# 2 - Imprima várias strings a explicar cada um dos jogos
print(f" {jogos[0]} é um jogo de tiros estratégico 5v5")
print(f" {jogos[1]} é um jogo de tiros battle royale com construção")
print(f" {jogos[2]} é um jogo de futebol elétronico")
# 3 - Insira na segunda posição da lista outro jogo e imrpima a lista
jogos.insert(1, "COD")
print(jogos)
# 4 - Ordene a lista e imprima
jogos.sort()
print(jogos)
# 5 - Reverta a lista  eimrpima
jogos.reverse()
print(jogos)