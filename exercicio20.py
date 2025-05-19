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
        return super().__str__() + f", Especialidade: {self.especialidade}, Nº Ordem: {self.numero_ordenados}"

class Paciente(Pessoa):
    def __init__(self, nome, idade, nif, numero_utente):
        super().__init__(nome, idade, nif)
        self.numero_utente = numero_utente
        self.historial_medico = []

    def adicionar_entrada_historial(self, descricao):
        self.historial_medico.append(descricao)

    def listar_historial(self):
        return "\n".join(self.historial_medico) if self.historial_medico else "Sem historial médico."

    def __str__(self):
        return super().__str__() + f", Nº Utente: {self.numero_utente}"

class Consulta:
    def __init__(self, data, medico, paciente, descricao):
        self.data = data
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao

    def __str__(self):
        return f"Data: {self.data}, Médico: {self.medico.nome}, Paciente: {self.paciente.nome}, Descrição: {self.descricao}"

medicos = []
pacientes = []
consultas = []

def registrar_medico(nome, idade, nif, especialidade, numero_ordenados):
    medicos.append(Medico(nome, idade, nif, especialidade, numero_ordenados))

def registrar_paciente(nome, idade, nif, numero_utente):
    pacientes.append(Paciente(nome, idade, nif, numero_utente))

def agendar_consulta(data, medico_idx, paciente_idx, descricao):
    if 0 <= medico_idx < len(medicos) and 0 <= paciente_idx < len(pacientes):
        consultas.append(Consulta(data, medicos[medico_idx], pacientes[paciente_idx], descricao))
    else:
        print("Índice inválido para médico ou paciente.")

def listar_medicos():
    print("\nMédicos cadastrados:")
    for i, medico in enumerate(medicos):
        print(f"{i}. {medico}")
    print()

def listar_pacientes():
    print("\nPacientes cadastrados:")
    for i, paciente in enumerate(pacientes):
        print(f"{i}. {paciente}")
    print()

def listar_consultas():
    print("\nConsultas agendadas:")
    for consulta in consultas:
        print(consulta)
    print()

def executar():
    registrar_medico("Dr. Ana", 45, "123456789", "Cardiologia", "9876")
    registrar_medico("Dr. João", 50, "987654321", "Ortopedia", "5432")
    registrar_paciente("Carlos Silva", 30, "111222333", "0001")
    registrar_paciente("Maria Souza", 25, "444555666", "0002")
    agendar_consulta("2025-04-05", 0, 0, "Check-up geral")
    agendar_consulta("2025-04-06", 1, 1, "Exame ortopédico")
    listar_medicos()
    listar_pacientes()
    listar_consultas()

executar()