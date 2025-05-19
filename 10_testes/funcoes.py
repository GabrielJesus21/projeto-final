from funcoes import calcular_imposto
from datetime import time

def test_calcular_imposto():
    assert calcular_imposto(100) == 22

def calcular_imposto(preco):
    return preco * 0.23

def processar_formulario(nome, idade):
    base_dados = []
    base_dados.append({"nome": nome})
    return base_dados

# funcao registar utilizador
def registar_utilizador(nome, senha):
    if nome and senha:
        return {"status": "sucesso", "mensagem": "Utilizador registado"}
    else:
        return {"status": "erro", "mensagem": "O Nome e a senha são obrigatórios"}
    
#funcao calculadora
def multiplicacao(x, y):
    return x * y

#funcao 
def somar_lista(lista):
    time.sleep(1)
    return sum(lista)

