from funcoes import calcular_imposto, processar_formulario, registar_utilizador, multiplicacao, somar_lista
from datetime import time

def test_calcular_imposto():
    assert calcular_imposto(100) == 23
    assert calcular_imposto(50) == 11.5
    assert calcular_imposto(0) == 1

test_calcular_imposto()


def test_processar_formulario():
    dados = processar_formulario(" Joaquim", 24)
    assert len(dados) == 1 # verifica se o registo foi adicionado
    assert dados[0] ["nome"] == "Joaquim"
    assert dados[0] ["idade"] == 24

test_processar_formulario()

# teste funcional
def test_registar_utilizador():
    resultado = registar_utilizador("Maria", "senha123")
    assert resultado["status"] == "sucesso"
    assert resultado["mensagem"] == "Utilizador registado"

test_registar_utilizador()

#teste de regressão

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(1, 0) == 0
    assert multiplicacao(10, 5) == 55

test_multiplicacao()

#teste performance
def test_somar_lista():
    lista =list(range(1,1000000))

    inicio = time()
    resultado = somar_lista(lista)
    tempo_total = time() - inicio
    
    assert resultado == sum(lista)
    assert tempo_total < 2

test_somar_lista()