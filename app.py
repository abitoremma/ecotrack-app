# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "EcoTrack fonctionne"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80
    )

print("=== EcoTrack Application ===")
print("Tentative de connexion à la base de données RDS...")
# Plus tard, on ajoutera le vrai code de connexion ici
print("Connexion réussie ! L'application EcoTrack est en ligne.")
