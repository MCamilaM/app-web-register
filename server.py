from flask import Flask, request, redirect, url_for, render_template
from database.db import *
from entities.client import Client
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/register_page")
def register_page():
    return render_template("register.html")
    
@app.route("/register_user", methods=["post"])
def register_user():
    dni = request.form["dni"]
    typeDocument = request.form["typeDocument"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    address = request.form["address"]
    phoneNumber = request.form["phoneNumber"]
    email = request.form["email"]
    
    client = Client(dni, typeDocument, name, lastname, address, phoneNumber, email)
    
    try:
        save_client(client)
        message = "Cliente registrado exitosamente"
    except Error as e:
        message = f"Fallo al registrar cliente: {e}"
    
    return redirect(url_for('list_clients', message=message))
    
    
@app.route("/clients", methods=["GET"])
def list_clients():
    clients = get_clients()
    print(clients)
    message = request.args.get('message')
    print(message)
    # Generar la tabla HTML
    tabla = ""
    if message is not None:
        tabla += f"<script> alert('{message}'); </script>"
    
    tabla += f"<h1>Lista de Clientes</h1> <table border='1'><tr><th>ID</th><th>DNI</th><th>Tipo de Documento</th><th>Nombre</th><th>Apellido</th><th>Dirección</th><th>Número de Teléfono</th><th>Correo Electrónico</th></tr>"
    for client in clients:
        tabla += f"<tr><td>{client[0]}</td><td>{html.escape(client[1])}</td><td>{html.escape(client[2])}</td><td>{html.escape(client[3])}</td><td>{html.escape(client[4])}</td><td>{html.escape(client[5])}</td><td>{html.escape(client[6])}</td><td>{html.escape(client[7])}</td></tr>"

    tabla += "</table>"

    return tabla

if __name__ == "__main__":
    host = "127.0.0.1"
    port = "8080"
    app.run(host, port)