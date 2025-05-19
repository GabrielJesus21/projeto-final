"Isto é uma string"
'Isto é uma string'
"""Isto é uma string"""

#Métodos
nome = "rui pedro"
print(nome.title()) #transforma a primeira letra das palavras em maiuscula
print(nome.upper()) #transforma todas as letras em maiusculas
print(nome.lower()) #transforma todas as letras em minusculas
print(nome.strip()) #retira espaços em branco no inicio e fim da string
print(nome.split()) #separa as palavras e retorna uma lista
print(nome.replace("rui", "Luís")) #substitui carateres numa string
print (len(nome))

#carateres de escape
# \n -> quebra de linha
# \t -> dá um tab
# \", \\, \' -> imprime caratere utilizado pela linguagem
url = "https://www.google.com"
print(url.removeprefix("https://www."))
print(url.removesuffix(".com"))

print("Linguagens de \"programação\"; \n\tPython\n\tJava")

#Slicing (fatiamento)
#         01234567890...
curso = "Fundamento de Python"
print(curso [15])
print(curso [:11])
print(curso [15:])
print(curso [15:17])
print(curso [-1:-7])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[::-1])
print(numeros[:4])

# Exercicios

#1 -> Crie uma variavel e atribua um nome, imprima o nome em maiusculas e minusculas

texto = "estamos no mês de Fevereiro"

print(texto.upper()) #transforma todas as letras em maiusculas
print(texto.lower())

#2 -> Insira uma variavel numa frase dentro da função print, utilize f-string

print (f"O nome é {nome} e é um grande senhor")

#3 -> Atraves do Slicing imprima o nome da empresa do url https://www.facebook.com (apenas facebook)

url2 = "https://www.facebook.com"

print(url2 [12:20])
