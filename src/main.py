from flask import Flask, url_for, session, request, redirect, render_template
import random
import csv
from pymongo import MongoClient
from paquete import Clase
import doctest
import os


# * Intanciar Flask
app = Flask(__name__)

# * Crear un llave/clave secreta para SESSION
app.config['SECRET_KEY'] = 'SUPER SECRETO'


# **************************************
# * ULR Conexion
MONGO_URL_ATLAS = 'mongodb+srv://Jorge:jorge@cluster0-7gqqa.mongodb.net/test?retryWrites=true&w=majority'

# * Establecer conexion
client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

# * Creacion base de datos MongoDB
db = client['sorteo']

# * Creacion coleccion
collection = db['examen']

@app.route('/')
def redireccionar():
    return redirect(url_for('home'))

# ******************************************
#* RUTE HOMRE
@app.route('/home')
def home():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        dni = request.form.get('dni')
        res = db.introducir_dni(nombre, dni)
        return render_template('home.html', res=res)
    return render_template('home.html')

# ******************************************
#*PAGE ERROR
@app.errorhandler(404)
def page_no_found(error):
    return '<h1> Pagina no encontrada, siga buscando</h1>'

# ******************************************
if __name__ == "__main__":
    app.run('0.0.0.0', '5000', debug=True)
