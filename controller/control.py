from flask import Flask, request, redirect, url_for, render_template, jsonify
from database.db import *
from entities.client import Client
from controller.admin_s3 import *
import html
import json

def home_page_ctrl():
    return render_template("home.html")
    
def register_page_ctrl():
    return render_template("register.html")
    
def register_user_ctrl():
    dni = request.form["dni"]
    typeDocument = request.form["typeDocument"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    address = request.form["address"]
    phoneNumber = request.form["phoneNumber"]
    email = request.form["email"]
    photo = request.files["photo"]
    
    client = Client(dni, typeDocument, name, lastname, address, phoneNumber, email)
    
    try:
        save_client(client)
        message = "Cliente registrado exitosamente"
        
        get_connection_s3()
    
        save_file(photo)

    except Error as e:
        message = f"Fallo al registrar cliente: {e}"
    
    return redirect(url_for('list_clients', message=message))
    
def consult_clients_ctrl():
    clients = get_clients()
    
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
    
def consult_client_ctrl():
    return render_template("consultClient.html")
    
def get_client_id_ctrl():
    
    data = request.get_json()
    dni = data['dni']

    if not dni:
        return "No se proporcionó el DNI"
        
    result = get_client_id(dni)
    
    if result:
        print(result)
        return jsonify({
            "dni": result[1],
            "typeDocument": result[2],
            "name": result[3],
            "lastname": result[4],
            "address": result[5],
            "phoneNumber": result[6],
            "email": result[7]
        })
        
    else:
        return jsonify(
            {"error": f"El cliente con DNI: {dni} no fue encontrado"})