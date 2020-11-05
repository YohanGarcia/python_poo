from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

from formularios.form import SerieForm, CapituloForm

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)

class Serie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50), nullable=True)
    sinopsis =  db.Column(db.Text(), nullable=True)
    img = db.Column(db.String(200), nullable=True)
    capitulo = db.relationship('Capitulo', backref='serie', lazy=True)
    
    
    def __repr__(self):
        return '<Serie %r>' % self.titulo

class Capitulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    serie_id = db.Column(db.Integer, db.ForeignKey('serie.id'), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():

    serie = Serie.query.all()
    return render_template('index.html', serie=serie)

@app.route('/directorio', methods=['GET', 'POST'])
def directorio():

    serie = Serie.query.all()
    return render_template('browse.html', serie=serie)

@app.route('/admin/sub-ser',  methods=('GET', 'POST'))
def subir_serie():
    form=SerieForm()
    if form.validate_on_submit():
        serie = Serie(titulo=form.titulo.data,
                     sinopsis=form.sinopsis.data,
                     img=form.img.data)
        db.session.add(serie)
        db.session.commit()
        flash('Serie enviada')
        return redirect(url_for('subir_serie'))
    return render_template('admin/subir-serie.html', form=form)

@app.route('/admin/sub-cap', methods=('GET', 'POST'))
def subir_capitulo():
    form=CapituloForm()
    ser = Serie.query.all()
    if form.validate_on_submit():
        serie_id = request.form.get('sele_serie')
        cap = Capitulo(name=form.capitulo.data, serie_id=serie_id)
        db.session.add(cap)
        db.session.commit()
        flash('Capitulo enviado')
        return redirect(url_for('index'))
    return render_template('admin/subir-cap.html', form=form, ser=ser)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000)