import PySimpleGUI as sg
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('dados.db')

# Criar a tabela Cliente caso ela não exista
conn.execute('''CREATE TABLE IF NOT EXISTS Cliente (
                    cpf VARCHAR(11) PRIMARY KEY,
                    nome VARCHAR(100),
                    email VARCHAR(100)
                )''')

# Criar a tabela Telefone caso ela não exista
conn.execute('''CREATE TABLE IF NOT EXISTS Telefone (
                    id_telefone INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero VARCHAR(20),
                    id_cliente_fk VARCHAR(11),
                    id_tipo_telefone_fk INT,
                    FOREIGN KEY (id_cliente_fk) REFERENCES Cliente(cpf)
                )''')

# Criar a tabela Endereco caso ela não exista
conn.execute('''CREATE TABLE IF NOT EXISTS Endereco (
                    id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente_fk VARCHAR(11),
                    rua VARCHAR(100),
                    id_tipo_fk INT,
                    id_estado_fk VARCHAR(2),
                    cep VARCHAR(8),
                    FOREIGN KEY (id_cliente_fk) REFERENCES Cliente(cpf),
                    FOREIGN KEY (id_tipo_fk) REFERENCES Tipo_Endereco(id_tipo),
                    FOREIGN KEY (id_estado_fk) REFERENCES Estado(sigla)
                )''')

# Função para cadastrar o cliente no banco de dados
def cadastrar_cliente(nome, cpf, email, numero_telefone, id_tipo_telefone, rua, id_tipo_endereco, id_estado, cep):
    try:
        # Inserir o cliente na tabela Cliente
        conn.execute("INSERT INTO Cliente (cpf, nome, email) VALUES (?, ?, ?)", (cpf, nome, email))
        
        # Obter o último ID do cliente inserido
        id_cliente = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        
        # Inserir o telefone do cliente na tabela Telefone
        conn.execute("INSERT INTO Telefone (numero, id_cliente_fk, id_tipo_telefone_fk) VALUES (?, ?, ?)",
                     (numero_telefone, id_cliente, id_tipo_telefone))
        
        # Inserir o endereço do cliente na tabela Endereco
        conn.execute("INSERT INTO Endereco (id_cliente_fk, rua, id_tipo_fk, id_estado_fk, cep) VALUES (?, ?, ?, ?, ?)",
                     (id_cliente, rua, id_tipo_endereco, id_estado, cep))
        
        # Commit das alterações no banco de dados
        conn.commit()
        
        return True, "Cliente cadastrado com sucesso!"
    
    except Exception as e:
        return False, f"Erro ao cadastrar cliente: {str(e)}"

# Layout da janela
layout = [
    [sg.Text("Nome:")],
    [sg.Input(key='-NOME-')],
    [sg.Text("CPF:")],
    [sg.Input(key='-CPF-')],
    [sg.Text("Email:")],
    [sg.Input(key='-EMAIL-')],
    [sg.Text("Telefone:")],
    [sg.Input(key='-TELEFONE-')],
    [sg.Text("Tipo de Telefone:")],
    [sg.Input(key='-TIPO_TELEFONE-')],
    [sg.Text("Rua:")],
    [sg.Input(key='-RUA-')],
    [sg.Text("Tipo de Endereço:")],
    [sg.Input(key='-TIPO_ENDERECO-')],
    [sg.Text("Estado:")],
    [sg.Input(key='-ESTADO-')],
    [sg.Text("CEP:")],
    [sg.Input(key='-CEP-')],
    [sg.Button("Cadastrar")]
]

# Criar a janela
window = sg.Window("Cadastro de Clientes", layout)

# Loop principal do programa
while True:
    event, values = window.read()
    
    # Finalizar o programa se a janela for fechada
    if event == sg.WINDOW_CLOSED:
        break
    
    # Cadastrar o cliente no banco de dados quando o botão "Cadastrar" for pressionado
    if event == "Cadastrar":
        nome = values['-NOME-']
        cpf = values['-CPF-']
        email = values['-EMAIL-']
        numero_telefone = values['-TELEFONE-']
        id_tipo_telefone = values['-TIPO_TELEFONE-']
        rua = values['-RUA-']
        id_tipo_endereco = values['-TIPO_ENDERECO-']
        id_estado = values['-ESTADO-']
        cep = values['-CEP-']
        
        resultado, mensagem = cadastrar_cliente(nome, cpf, email, numero_telefone, id_tipo_telefone, rua, id_tipo_endereco, id_estado, cep)
        
        if resultado:
            sg.popup(mensagem, title="Sucesso")
        else:
            sg.popup(mensagem, title="Erro")
    
# Fechar a conexão com o banco de dados
conn.close()
