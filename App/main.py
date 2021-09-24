'''
    Controlador principal de nuestra aplicacion
'''
# Importamos la librerias necesarias para el proyectoS
import re
from flask import Flask, render_template, request
from flask.helpers import get_debug_flag, url_for
from werkzeug.utils import redirect

from Registro import Registro
from db import DB_Control

# Creamos nuestro objeto aplicacion
app = Flask(__name__)
bd = r"/home/ldavid/Proyectos/Py_proj/POO/App/database.db"
tabla = "registro"

gbd = DB_Control(bd, tabla)
gbd.crear_tabla()
gbd.cerrar_cnx()


# Creamos nuestra primera ruta
@app.route("/")
def inicio():
    return render_template("inicio.html")

#Creamos una ruta para el registro, capas de resolver peticiones get y post
@app.route("/registro", methods = ['Get', 'Post'])

def registro():
    if request.method == "POST":
        reg = Registro(
            request.form['_nombre'],
            request.form['_edad'],
            request.form['_correo'],
            request.form['_ciudad'],
            request.form['_usuario'],
            request.form['_clave']
        )
        # Abrimos conexion
        gbd.abrir_cnx()
        # Buscamos si el registro ya existe
        resultado, data = gbd.busqueda("usuario",reg.usuario)
        if resultado == True:
            return "Usuario ya existe"
        gbd.registrar(reg)

        print(reg.edad)
        return(f"Nombre: {reg.nombre} | Correo: {reg.correo}")

    elif request.method == "GET":
        return render_template('registro.html')

# Creamos nuestra pantalla login, capaz de recibir peticiones get y post
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        return redirect(url_for('dash'))
    else:
        return render_template('login.html')   


@app.route("/dash")
def dash():
    return "Bienvenido"


if (__name__ == "__main__"):
    app.run(debug = True, port = 5000)