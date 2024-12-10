from app import app
from app.controllers import usuarios, seguidores  # Importa ambos controladores

if __name__ == "__main__":
    app.run(debug=True)