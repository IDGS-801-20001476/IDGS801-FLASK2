from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  FieldList, FormField, SelectField
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):

    matricula = StringField('Matricula',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 5 min and 5 max')
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')
    ])
    apaterno = StringField('Apaterno',[mi_validacion])
    amaterno = StringField('Amaterno')
    email =  EmailField('Correo')

class LoginForm(Form):
    username=StringField('usuario',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 5 min and 5 max')
    ])
    password=StringField('password',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='long de campo 5 min and 5 max')
    ])

class TraductorGuardar(Form):
    espanol = StringField('Español', [
        validators.DataRequired(message='Ingresa una palabra español'),
        validators.InputRequired()])
    ingles = StringField('Inglés', [ 
        validators.DataRequired(message='Ingresa una palabra en inglés'),
         validators.InputRequired()])


class TraductorBuscar(Form):
    buscar_palabra = StringField('Palabra', [ 
        validators.DataRequired(message='Ingresa una palabra para buscarla'),
        validators.InputRequired()])
    respuesta = RadioField('Idioma de búsqueda', choices=[('es', 'Español'), ('en', 'Inglés')],
        validators=[validators.InputRequired(message='Seleccione una opción')])