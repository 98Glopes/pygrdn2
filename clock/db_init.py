import sqlite3

# conectando...
conn = sqlite3.connect('database.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE alarm (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        hour TEXT,
		behavior TEXT
);
""")
cursor.execute("""
CREATE TABLE config (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		max_watermark NUMERIC,
		min_watermark NUMERIC,
		max_temp NUMERIC,
		min_temp NUMERIC,
		max_hygro NUMERIC,
		min_hygro NUMERIC		
);
""")
cursor.execute("""
CREATE TABLE error_log (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		error_code TEXT,
		error_desc TEXT,
		obs TEXT
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()