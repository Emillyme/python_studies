import sqlite3

# criando tabela ---------------------------
# sqlite3.connect('historio.db') as conexao:
# cursor = conexao.cursor()
# cursor.execute(''' CREATE TABLE historico (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                     nome TEXT NOT NULL,
#                     idade INT NOT NULL);''')

# inserir dados na tabela ---------------------
# cursor.execute(''' INSERT INTO historico (nome, idade) VALUES('Miro', 55)''')

# salvar dados ------------------
# conexao.commit()

# Transações --------------
with sqlite3.connect('historio.db') as conexao:
    conexao.execute('BEGIN')
    cursor = conexao.cursor()
    cursor.execute(''' INSERT INTO historico (nome, idade) VALUES('Ana Isabela', 45)''')
    cursor.execute(''' INSERT INTO historico (nome, idade) VALUES('Joaquim', 95)''')
    cursor.execute(''' INSERT INTO historico (nome, idade) VALUES('Maria', 35)''')
    cursor.execute(''' INSERT INTO historico (nome, idade) VALUES('Emilia', 19)''')
    conexao.commit()


# Atualizando os dados ----------------------
with sqlite3.connect('historio.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute(''' UPDATE historico SET nome='Pedro', idade=2 WHERE id=1''')
    conexao.commit()


# Deletando dados ----------------------
with sqlite3.connect('historio.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute('''  DELETE FROM historico WHERE idade < 18''')
    conexao.commit()


# imprimindo os dados --------------
with sqlite3.connect('historio.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute(''' SELECT * FROM historico''')
    resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

