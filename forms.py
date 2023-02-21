from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  FieldList, FormField, SelectField
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField


class UserForm(Form):
    nombre = StringField('Matricula')
    nombre = StringField('Nombre')
    apaterno = StringField('Apaterno')
    amaterno = StringField('Amaterno')
    email =  EmailField('Correo')