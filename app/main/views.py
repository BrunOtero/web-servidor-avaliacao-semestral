from flask import render_template, redirect, url_for, flash
from .. import db
from ..models import Professor, Disciplina
from . import main
from .forms import NewProfessorForm
from datetime import datetime


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@main.route('/professores', methods=['GET', 'POST'])
def professores():
    form = NewProfessorForm()
    professors = Professor.query.all()

    if form.validate_on_submit():
        nome_professor = form.professor.data
        disciplina_id = form.subject.data
        disciplina = Disciplina.query.get(disciplina_id)

        if disciplina:
            professor = Professor.query.filter_by(nome=nome_professor).first()

            if professor:
                flash("Professor já existe na base de dados!", 'warning')

            else:
                professor = Professor(nome=nome_professor)
                professor.disciplinas.append(disciplina)
                db.session.add(professor)
                db.session.commit()

        return redirect(url_for('.professores'))
    return render_template(
                            'professors.html',
                            form=form,
                            professors=professors,
                            current_time=datetime.utcnow()
                        )



@main.route('/disciplinas', methods=['GET'])
def disciplinas():
    return render_template('notAvailable.html', current_time=datetime.utcnow())

@main.route('/alunos', methods=['GET'])
def alunos():
    return render_template('notAvailable.html', current_time=datetime.utcnow())

@main.route('/cursos', methods=['GET'])
def cursos():
    return render_template('notAvailable.html', current_time=datetime.utcnow())

@main.route('/ocorrencias', methods=['GET'])
def ocorrencias():
    return render_template('notAvailable.html', current_time=datetime.utcnow())
