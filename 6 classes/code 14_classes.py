# criar classe pessoa
class Pessoa:
        def __init__(self, nome, idade):
                self.nome = nome
                self.idade = idade
                







# esqueci de meter isto tudo

saldo_inicial = float(input("Insira o saldo inicial"))
conta1 = ContaBancaria(saldo_inicial)
opcao = ""
while opcao != "s":
        quantia_depositada = float(input("Insira a quantia a depositar"))
        quantia_levantada = float(input("Insira a quantia a levantar"))

        conta1 = ContaBancaria(saldo_inicial)
        conta1.depositar(quantia_depositada)
        conta1.consultar_saldo()
        conta1.levantar(quantia_levantada)
        conta1.consultar_saldo()

        opcao = input ("Quer terminar o programa? (s para sair, enter para continuar): ").lower()