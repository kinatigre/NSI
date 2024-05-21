import flask

app = flask.Flask(__name__)

# Chemin du fichier de données
data_file = "Quiz/data.txt"

# Charger les données depuis le fichier
def load_data():
    data = []
    with open(data_file, 'r', encoding='utf-8') as file:
        for line in file:
            nom,point = line.split(',')
            data.append([nom,point])
    return data

# Sauvegarder les données dans le fichier
def save_data(data):
    with open(data_file, 'w', encoding='utf-8') as file:
        for item in data:
            ligne = ','.join(item).strip() + '\n'
            file.write(ligne)

# Route pour la page d'accueil
@app.route('/')
def index():
    data = load_data()
    # Trier les données par ordre croissant de points
    data.sort(key=lambda x: int(x[1]), reverse=True)
    return flask.render_template('index.html', data=data)

# Route pour ajouter une nouvelle entrée
@app.route('/add', methods=['POST'])
def add():
    nom = flask.request.form['nom']
    point = flask.request.form['point']
    data = load_data()
    data.append([nom, point])
    save_data(data)
    return flask.redirect(flask.url_for('index'))

app.run(debug=True)