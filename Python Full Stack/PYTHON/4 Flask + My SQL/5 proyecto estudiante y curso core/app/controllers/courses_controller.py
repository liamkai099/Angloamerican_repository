from flask import render_template, redirect, request, url_for
from app import app
from app.models.course import Course

@app.route('/cursos', methods=['GET', 'POST'])
def cursos():
    if request.method == 'POST':
        data = {"nombre": request.form['nombre']}
        Course.save(data)
        return redirect(url_for('cursos'))
    cursos = Course.get_all()
    return render_template('curso.html', cursos=cursos)

@app.route('/cursos/<int:id>')
def mostrar_curso(id):
    curso = Course.get_by_id(id)
    from app.models.student import Student
    estudiantes = Student.get_all_by_course(id)
    return render_template('mostrar_curso.html', curso=curso, estudiantes=estudiantes)
