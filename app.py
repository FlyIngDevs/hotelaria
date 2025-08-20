from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

def criar_conexao():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/")
def listar_clientes():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT usuario.nome, quartos.numero_quarto, usuario.fone
        FROM usuario
        JOIN quartos ON usuario.cpf = quartos.cpf
    ''')
    dados = cursor.fetchall()
    conn.close()
    
    # Convertendo os dados para uma lista de dicionários
    clientes = [{'nome': row[0], 'numero_quarto': row[1], 'fone': row[2]} for row in dados]
    
    return render_template('index.html', cliente=clientes)
    

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    telefone = request.form.get('fone')
    endereco = request.form.get('endereco')
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (nome, cpf, email, fone, endereco) VALUES (?, ?, ?, ?, ?)",
                   (nome, cpf, email, telefone, endereco))
    conn.commit()
    conn.close()
    return 'Usuário cadastrado com sucesso!'

@app.route('/excluir-cliente', methods=['POST'])
def excluir_cliente():
    cpf = request.form['cpf']
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuario WHERE cpf = ?', (cpf,))
    cursor.execute('DELETE FROM quartos WHERE cpf = ?', (cpf,))
    conn.commit()
    conn.close()
    return 'Cliente excluído com sucesso!'

@app.route('/cadastrar-quarto', methods=['POST'])
def cadastrar_quarto():
    cpf = request.form['cpf']
    numero_quarto = request.form['numero_quarto']
    anotacoes = request.form['anotacoes']
    conn = criar_conexao()
    cursor = conn.cursor()
    
    # Verificar se o cliente existe
    cursor.execute('SELECT * FROM usuario WHERE cpf = ?', (cpf,))
    cliente = cursor.fetchone()
    if not cliente:
        conn.close()
        return 'Cliente não encontrado.'
    
    # Verificar se o quarto já está cadastrado para outro CPF
    cursor.execute('SELECT * FROM quartos WHERE numero_quarto = ?', (numero_quarto,))
    quarto = cursor.fetchone()
    if quarto:
        conn.close()
        return 'O quarto já está cadastrado para outro cliente.'
    
    # Inserir o novo quarto
    cursor.execute('INSERT INTO quartos (cpf, numero_quarto, anotacoes) VALUES (?, ?, ?)', (cpf, numero_quarto, anotacoes))
    conn.commit()
    conn.close()
    return 'Quarto cadastrado com sucesso e vinculado ao cliente!'


if __name__ == '__main__':
    app.run(debug=True)