import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('database.db')

# Criando um cursor
cursor = conn.cursor()

# Criando a tabela "cliente"
cursor.execute('CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, email TEXT, fone VARCHAR(20), endereco TEXT)')

# Criando a tabela de quartos
cursor.execute('CREATE TABLE IF NOT EXISTS quarto (id INTEGER PRIMARY KEY AUTOINCREMENT, numero_quarto TEXT, anotacoes TEXT, cliente_id INTEGER, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')

# Excluit tabela
cursor.execute("DROP TABLE ''quarto''")

#Excluir dados da tabela
cursor.execute("DELETE FROM ''usuario'' ")
# Confirmando a transação
conn.commit()

# Fechando a conexão
conn.close()

