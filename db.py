import sqlite3

# conectando...
conn = sqlite3.connect('database.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE pictures (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        picture TEXT
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()