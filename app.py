from flask import Flask,render_template
from flask import request

from collections import Counter

import forms
import actividad1


app= Flask(__name__)

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")


@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=' '
    nom=' '
    if request.method == 'POST':
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

if __name__ == "__main__":
    app.run(debug=True,port=3000)


