from controller.control import *
from server import app

@app.route("/")
def home():
    return home_page_ctrl()
    
@app.route("/register_page")
def register_page():
    return register_page_ctrl()
    
@app.route("/register_user", methods=["post"])
def register_user():
    return register_user_ctrl()
    
@app.route("/clients", methods=["GET"])
def list_clients():
    return consult_clients_ctrl()
    
@app.route("/consultClient", methods=["get"])
def consult_client():
    return consult_client_ctrl()

@app.route("/consultClientId", methods=["post"])
def consult_client_id():
    return get_client_id_ctrl()