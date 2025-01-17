from . import db

# Tabela associativa para muitos-para-muitos
professor_disciplina = db.Table(
    'professor_disciplina',
    db.Column('professor_id', db.Integer, db.ForeignKey('professores.id'), primary_key=True),
    db.Column('disciplina_id', db.Integer, db.ForeignKey('disciplinas.id'), primary_key=True)
)

class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True)
    disciplinas = db.relationship(
        'Disciplina',
        secondary=professor_disciplina,  # Relação muitos-para-muitos
        backref=db.backref('professores', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return f'<Professor {self.nome}>'


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return f'<Disciplina {self.nome}>'