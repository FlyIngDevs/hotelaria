# import sqlite3

# cliente = [
#             {"nome":"Leonardo Ferreira", "cpf":"38565985252", "email":"leo@hotmail.com", "fone":"987343848", "endereco":"rua ulhoa Cinta 196" },
#             {"nome":"Leonardo Ferreira", "cpf":"38565985252", "email":"leo@hotmail.com", "fone":"987343848", "endereco":"rua ulhoa Cinta 196" },
#             {"nome":"Leonardo Ferreira", "cpf":"38565985252", "email":"leo@hotmail.com", "fone":"987343848", "endereco":"rua ulhoa Cinta 196" }

    
# ]

# conn = sqlite3.connect('schema.db')

# cursor = conn.cursor()

# for clientes in cliente:
#     cursor.execute(""" 
#         INSERT INTO cliente (nome, cpf, email, fone, endereco)
#         VALUES (?, ?, ?, ?, ?)

#         """, (clientes['nome'], clientes['cpf'], clientes['email'], clientes['fone'], clientes['endereco']))
    
# print('dados inserido com sucesso')
    
# conn.commit()
# conn.close()