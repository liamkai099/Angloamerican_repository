from flask import request, redirect, flash
from app import app
from app.models.seguidor import Seguidor

@app.route("/agregar_seguidor", methods=["POST"])
def agregar_seguidor():
    # Procesa la adición de un nuevo seguidor
    data = {
        "usuario_id": request.form["usuario_id"],
        "seguidor_id": request.form["seguidor_id"]
    }

    # Validación para evitar que un usuario se siga a sí mismo
    if data["usuario_id"] == data["seguidor_id"]:
        flash("Un usuario no puede seguirse a sí mismo.")
        return redirect("/usuarios")

    # Validación para evitar duplicados
    if not Seguidor.is_duplicate(data):  # Verifica si existe un método funcional en el modelo
        Seguidor.save(data)
        flash("Seguidor agregado exitosamente")
    else:
        flash("El seguidor ya está conectado a este usuario.")
    return redirect("/usuarios")
