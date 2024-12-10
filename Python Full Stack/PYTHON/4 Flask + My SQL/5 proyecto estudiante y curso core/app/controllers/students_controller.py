from flask import render_template, redirect, request, url_for
from app import app
from app.models.student import Student
from app.models.course import Course

@app.route('/estudiante', methods=['GET', 'POST'])
def nuevo_estudiante():
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'edad': request.form['edad'],
            'curso_id': request.form['curso']
        }
        Student.save(data)
        return redirect(url_for('cursos'))
    cursos = Course.get_all()
    return render_template('nuevo_estudiante.html', cursos=cursos)
