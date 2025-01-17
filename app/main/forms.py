from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from ..models import Disciplina  # Importe o modelo de Disciplina

class NewProfessorForm(FlaskForm):
    professor = StringField('Cadastre o novo Professor:', validators=[DataRequired()])
    subject = SelectField('Disciplina associada:', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Carrega as disciplinas do banco de dados
        self.subject.choices = [(disciplina.id, disciplina.nome) for disciplina in Disciplina.query.all()]
