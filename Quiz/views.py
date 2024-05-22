import flask, os

app = flask.Flask(__name__)

# Chemin du fichier de données
data_file = os.path.join(os.path.dirname(__file__), "data.txt")

# Charger les données depuis le fichier
def load_data():
    data = []
    with open(data_file, "r") as file:
        for line in file:
            nom,point = line.split(",")
            data.append([nom,point])
            print(data)
    return data

# Sauvegarder les données dans le fichier
def save_data(data):
    with open(data_file, "w", encoding="utf-8") as file:
        for item in data:
            ligne = ",".join(item).strip() + "\n"
            file.write(ligne)

# Route pour la page d"accueil
@app.route("/")
def index():
    return flask.render_template("login.html")

@app.route("/qcm")
def qcm():
    nom = flask.request.args.get("nom")
    return flask.render_template("qcm.html", nom=nom)

@app.route("/score")
def score():
    nom = flask.request.args.get("nom")
    point = flask.request.args.get("point")
    data = load_data()
    data.sort(key=lambda x: int(x[1]), reverse=True) # Trier les données par ordre croissant de points
    return flask.render_template("score.html", data=data, nom=nom, point=point)

# Route pour ajouter une nouvelle entrée
@app.route("/add", methods=["POST"])
def add():
    nom = flask.request.form["nom"]
    point = flask.request.form["point"]
    data = load_data()
    data.append([nom, point])
    save_data(data)
    return flask.redirect(flask.url_for("score", nom=nom, point=point))

app.run(debug=True)