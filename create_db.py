import sqlite3

# Créer la base de données et la table finances
conn = sqlite3.connect('database.db')
conn.execute('''
    CREATE TABLE IF NOT EXISTS finances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        revenus REAL,
        depenses REAL,
        budget REAL,
        interets REAL,
        solde REAL,
        interets_calcules REAL
    )
''')
conn.commit()
conn.close()
