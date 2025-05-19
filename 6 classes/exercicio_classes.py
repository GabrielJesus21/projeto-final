class Restaurante:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.ementa = []  # Lista de pratos disponíveis
        self.pedidos = []  # Lista de pedidos feitos
        
    # Método para adicionar um prato à ementa
    def adicionar_prato(self, prato):
        if prato not in self.ementa:
            self.ementa.append(prato)
            print(f"Prato '{prato}' adicionado à ementa.")
        else:
            print(f"Prato '{prato}' já está na ementa.")
    
    # Método para remover um prato da ementa
    def remover_prato(self, prato):
        if prato in self.ementa:
            self.ementa.remove(prato)
            print(f"Prato '{prato}' removido da ementa.")
        else:
            print(f"Prato '{prato}' não está na ementa.")

    # Método para registrar um pedido de um cliente
    def fazer_pedido(self, cliente, prato):
        prato = prato.strip()  # Remover espaços em branco ao redor do nome do prato
        if prato in self.ementa:
            self.pedidos.append((cliente, prato))
            print(f"Pedido de {cliente} registado: {prato}.")
        else:
            print(f"Pedido inválido: '{prato}' não está na ementa.")
    
    # Método para listar todos os pedidos feitos
    def listar_pedidos(self):
        if self.pedidos:
            print("Pedidos realizados:")
            for cliente, prato in self.pedidos:
                print(f"{cliente} pediu {prato}")
        else:
            print("Ainda não foram feitos pedidos.")


# Criação do objeto Restaurante
restaurante = Restaurante("Sabores da Vila", "Rua dos Gulosos, 23")

# Adicionar pratos ao cardápio
restaurante.adicionar_prato("Arroz de Marisco")
restaurante.adicionar_prato("Bolonhesa")
restaurante.adicionar_prato("Bife Grelhado")

# Realizar pedidos
restaurante.fazer_pedido("João", "Bolonhesa")
restaurante.fazer_pedido("Maria", "Arroz de Marisco")
restaurante.fazer_pedido("Carlos", "Pizza")  # Pedido inválido

# Listar todos os pedidos
restaurante.listar_pedidos()

# Remover um prato da ementa
restaurante.remover_prato("Bife Grelhado")
restaurante.remover_prato("Pizza")  # Tentativa de remover um prato que não está na ementa

# Verificar a ementa após a remoção
print(f"Ementa atual: {restaurante.ementa}")
