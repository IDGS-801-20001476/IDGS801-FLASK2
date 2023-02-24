from flask import Flask,render_template
from flask import request
from flask import make_response 
from flask import   flash
from flask_wtf import CSRFProtect


from collections import Counter

import forms
import actividad1


app= Flask(__name__)

app.config['SECRET_KEY']="esta es tu clave encriptada"
csrf=CSRFProtect()

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")



@app.route("/cookie", methods=['GET','POST'])
def cookie():
    reg_user=forms.LoginForm(request.form)

    response=make_response(render_template('cookie.html', form=reg_user))
    if request.method == 'POST' and reg_user.validate():
        user=reg_user.username.data
        pasw=reg_user.password.data
        datos=user+"@"+pasw
        success_message='Bienvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(success_message)
    response=make_response(render_template('cookie.html', form=reg_user))
        #print(user + ' '+ pasw)
    return response





@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=' '
    nom=' '
    if request.method == 'POST' and reg_alum.validate():
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template ('Alumnos.html', form=reg_alum,mat=mat,nom=nom)



@app.route("/CajasDinamicas", methods=['GET','POST'])
def CajasDi():
    reg_caja=actividad1.CajaForm(request.form)
    if request.method=='POST':
        btn = request.form.get("btn")
        if btn == 'Enviar':
            return render_template('actividad1.html',form=reg_caja)
        if btn == 'Resultados':
            numero = request.form.getlist("numeros")
            max_value = None
            for num in numero:
                if (max_value is None or num > max_value):
                    max_value = num

            min_value = None
            for num in numero:
                if (min_value is None or num < min_value):
                    min_value = num

            for i in range(len(numero)):
                numero[i] = int(numero[i])


            prom = 0
            prom = sum(numero) / len(numero)

            counter = Counter(numero)
            resultados = counter.most_common()
            textoResultado = ''
            for r in resultados:
                if r[1] > 1:
                   textoResultado += '<p>El número {0} se repite: {1} veces </p>'.format(r[0], r[1])
            return render_template('resultadosActividad1.html',form=reg_caja, max_value=max_value, min_value=min_value, prom=prom, repetidos = textoResultado)
    return render_template('actividad1.html', form=reg_caja)


@app.route("/Traductor",methods=['GET','POST'])
def traductor():
    
    Guardar = forms.TraductorGuardar(request.form)
    Buscar = forms.TraductorBuscar(request.form)
    result = ''

    if request.method == 'POST' and 'guardar' in request.form:
        if Guardar.validate():
            espanolP = Guardar.espanol.data.upper()
            inglesP = Guardar.ingles.data.upper()

          
            with open('traductor.txt', 'a') as file:
                file.write(espanolP + '=' + inglesP + '\n')
    if request.method == 'POST' in request.form:
       return render_template('traductor.html', formGuardar=Guardar, formBuscar=Buscar, result=result)

    if request.method == 'POST' and 'buscar' in request.form:
        if Buscar.validate():
            palabraBuscar = Buscar.buscar_palabra.data.upper()
            idioma = Buscar.respuesta.data

           
            with open('traductor.txt', 'r') as file:
                for line in file:
                    spanish, english = line.strip().split('=')
                    if idioma == 'es' and spanish == palabraBuscar:
                        result = english
                        break
                    elif idioma == 'en' and english == palabraBuscar:
                        result = spanish
                        break
                else:
                    result = 'Palabra no encontrada'
    if request.method == 'POST' in request.form:
       return render_template('traductor.html', Guardar=Guardar, Buscar=Buscar, result=result)
    return render_template('traductor.html', Guardar=Guardar, Buscar=Buscar, result=result)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)


