class Pessoa:
    def __init__(self, nome, idade, nif):
        self.nome = nome
        self.idade = idade
        self.nif = nif
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, NIF: {self.nif}"

class Medico(Pessoa):
    def __init__(self, nome, idade, nif, especialidade, numero_ordenados):
        super().__init__(nome, idade, nif)
        self.especialidade = especialidade
        self.numero_ordenados = numero_ordenados
    
    def __str__(self):
        return f"{super().__str__()}, Especialidade: {self.especialidade}, Nº Ordenados: {self.numero_ordenados}"

class Paciente(Pessoa):
    def __init__(self, nome, idade, nif, numero_utente):
        super().__init__(nome, idade, nif)
        self.numero_utente = numero_utente
        self.historial_medico = []
    
    def adicionar_entrada_historial(self, descricao):
        self.historial_medico.append(descricao)
    
    def listar_historial(self):
        return "\n".join(self.historial_medico) if self.historial_medico else "Sem historial"
    
    def __str__(self):
        return f"{super().__str__()}, Nº Utente: {self.numero_utente}"

class Consulta:
    def __init__(self, data, medico, paciente, descricao):
        self.data = data
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
    
    def __str__(self):
        return f"Data: {self.data}, Médico: {self.medico.nome}, Paciente: {self.paciente.nome}, Descrição: {self.descricao}"

def main():
    medicos = []
    pacientes = []
    consultas = []
    
    while True:
        
        print("\n1. Criar médico")
        print("2. Listar médicos")
        print("3. Criar paciente")
        print("4. Listar pacientes")
        print("5. Agendar consulta")
        print("6. Listar consultas")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            nif = input("NIF: ")
            especialidade = input("Especialidade: ")
            numero_ordenados = input("Nº Ordenados: ")
            medicos.append(Medico(nome, idade, nif, especialidade, numero_ordenados))
        
        elif opcao == "2":
            for medico in medicos:
                print(medico)
        
        elif opcao == "3":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            nif = input("NIF: ")
            numero_utente = input("Nº Utente: ")
            pacientes.append(Paciente(nome, idade, nif, numero_utente))
        
        elif opcao == "4":
            for paciente in pacientes:
                print(paciente)
        
        elif opcao == "5":
            data = input("Data: ")
            medico_idx = int(input("Índice do médico (0 a {}): ".format(len(medicos)-1)))
            paciente_idx = int(input("Índice do paciente (0 a {}): ".format(len(pacientes)-1)))
            descricao = input("Descrição: ")
            consultas.append(Consulta(data, medicos[medico_idx], pacientes[paciente_idx], descricao))
        
        elif opcao == "6":
            for consulta in consultas:
                print(consulta)
        
        elif opcao == "7":
            break

if __name__ == "__main__":
    medico1 = Medico("João Silva", 45, "123456789", "Cardiologia", "M001")
    medico2 = Medico("Maria Santos", 38, "987654321", "Pediatria", "M002")
    
    paciente1 = Paciente("Ana Costa", 30, "111222333", "P001")
    paciente1.adicionar_entrada_historial("Gripe em 2023")
    paciente2 = Paciente("Pedro Lima", 25, "444555666", "P002")
    paciente2.adicionar_entrada_historial("Alergia em 2024")
    
    consulta1 = Consulta("2025-04-05", medico1, paciente1, "Check-up anual")
    consulta2 = Consulta("2025-04-06", medico2, paciente2, "Consulta de rotina")
    
    main()