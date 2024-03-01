# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(_name_)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = StringField('Age')
    submit = SubmitField('Register')


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        existing_student = Student.query.filter_by(email=email).first()
        if existing_student:
            flash('Email already registered!')
            return redirect(url_for('register'))
        else:
            name = form.name.data
            age = form.age.data
            new_student = Student(email=email, name=name, age=age)
            db.session.add(new_student)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)

if _name_ == '_main_':
    db.create_all()
    app.run(debug=True)