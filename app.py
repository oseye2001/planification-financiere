from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Fonction pour récupérer les finances depuis la base de données
def recuperer_finances():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT * FROM finances ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'revenus': row[1],
            'depenses': row[2],
            'budget': row[3],
            'interets': row[4],
            'solde': row[5],
            'interets_calcules': row[6]
        }
    else:
        return {
            'revenus': 0,
            'depenses': 0,
            'budget': 0,
            'interets': 0,
            'solde': 0,
            'interets_calcules': 0
        }

# Fonction pour insérer des finances dans la base de données
def inserer_finances(revenus, depenses, budget, interets, solde, interets_calcules):
    conn = sqlite3.connect('database.db')
    conn.execute('''
        INSERT INTO finances (revenus, depenses, budget, interets, solde, interets_calcules)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (revenus, depenses, budget, interets, solde, interets_calcules))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    finances = recuperer_finances()
    return render_template('index.html', **finances)

@app.route('/mettre-a-jour', methods=['POST'])
def mettre_a_jour():
    revenus = float(request.form['revenus'])
    depenses = float(request.form['depenses'])
    budget = float(request.form['budget'])
    interets = float(request.form['interets'])
    
    solde = revenus - depenses
    interets_calcules = (solde * interets) / 100
    
    inserer_finances(revenus, depenses, budget, interets, solde, interets_calcules)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
