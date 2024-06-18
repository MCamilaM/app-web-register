{"filter":false,"title":"server.py","tooltip":"/server.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":38,"column":4},"end":{"row":45,"column":16},"action":"insert","lines":["# Generar la tabla HTML","    tabla = \"<table><tr><th>ID</th><th>DNI</th><th>Tipo de Documento</th><th>Nombre</th><th>Apellido</th><th>Dirección</th><th>Número de Teléfono</th><th>Correo Electrónico</th></tr>\"","    for resultado in resultados:","        tabla += f\"<tr><td>{resultado[0]}</td><td>{html.escape(resultado[1])}</td><td>{html.escape(resultado[2])}</td><td>{html.escape(resultado[3])}</td><td>{html.escape(resultado[4])}</td><td>{html.escape(resultado[5])}</td><td>{html.escape(resultado[6])}</td><td>{html.escape(resultado[7])}</td></tr>\"","","    tabla += \"</table>\"","","    return tabla"],"id":433}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":11},"action":"remove","lines":["clients"],"id":434},{"start":{"row":35,"column":4},"end":{"row":35,"column":14},"action":"insert","lines":["resultados"]}],[{"start":{"row":36,"column":10},"end":{"row":36,"column":17},"action":"remove","lines":["clients"],"id":435},{"start":{"row":36,"column":10},"end":{"row":36,"column":20},"action":"insert","lines":["resultados"]}],[{"start":{"row":2,"column":34},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":436}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":11},"action":"insert","lines":["import html"],"id":437}],[{"start":{"row":40,"column":13},"end":{"row":40,"column":39},"action":"insert","lines":["<h1>Lista de Clientes</h1>"],"id":438}],[{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"insert","lines":[" "],"id":439}],[{"start":{"row":40,"column":40},"end":{"row":40,"column":47},"action":"remove","lines":["<table>"],"id":440},{"start":{"row":40,"column":40},"end":{"row":40,"column":58},"action":"insert","lines":["<table border=\"1\">"]}],[{"start":{"row":40,"column":54},"end":{"row":40,"column":55},"action":"remove","lines":["\""],"id":441}],[{"start":{"row":40,"column":54},"end":{"row":40,"column":55},"action":"insert","lines":["'"],"id":442}],[{"start":{"row":40,"column":57},"end":{"row":40,"column":58},"action":"insert","lines":["'"],"id":443}],[{"start":{"row":40,"column":57},"end":{"row":40,"column":58},"action":"remove","lines":["'"],"id":444}],[{"start":{"row":40,"column":57},"end":{"row":40,"column":58},"action":"insert","lines":["'"],"id":445}],[{"start":{"row":40,"column":57},"end":{"row":40,"column":58},"action":"remove","lines":["'"],"id":446},{"start":{"row":40,"column":56},"end":{"row":40,"column":57},"action":"remove","lines":["\""]}],[{"start":{"row":40,"column":56},"end":{"row":40,"column":57},"action":"insert","lines":["'"],"id":447}],[{"start":{"row":0,"column":0},"end":{"row":52,"column":23},"action":"remove","lines":["from flask import Flask, render_template, request","from database.db import *","from entities.client import Client","import html","","app = Flask(__name__)","","@app.route(\"/\")","def home():","    return render_template(\"home.html\")","    ","@app.route(\"/register_page\")","def register_page():","    return render_template(\"register.html\")","    ","@app.route(\"/register_user\", methods=[\"post\"])","def register_user():","    dni = request.form[\"dni\"]","    typeDocument = request.form[\"typeDocument\"]","    name = request.form[\"name\"]","    lastname = request.form[\"lastname\"]","    address = request.form[\"address\"]","    phoneNumber = request.form[\"phoneNumber\"]","    email = request.form[\"email\"]","    ","    try:","        save_client(client)","        message = \"Usuario registrado exitosamente\"","    except Error as e:","        message = f\"Fallo al registrar usuario: {e}\"","    ","    return redirect(url_for('list_clients', message=message))","    ","    ","@app.route(\"/clients\", methods=[\"GET\"])","def list_clients():","    resultados = get_clients()","    print(resultados)","    message = request.args.get('message')","    # Generar la tabla HTML","    tabla = \"<h1>Lista de Clientes</h1> <table border='1'><tr><th>ID</th><th>DNI</th><th>Tipo de Documento</th><th>Nombre</th><th>Apellido</th><th>Dirección</th><th>Número de Teléfono</th><th>Correo Electrónico</th></tr>\"","    for resultado in resultados:","        tabla += f\"<tr><td>{resultado[0]}</td><td>{html.escape(resultado[1])}</td><td>{html.escape(resultado[2])}</td><td>{html.escape(resultado[3])}</td><td>{html.escape(resultado[4])}</td><td>{html.escape(resultado[5])}</td><td>{html.escape(resultado[6])}</td><td>{html.escape(resultado[7])}</td></tr>\"","","    tabla += \"</table>\"","","    return tabla","    #return render_template(\"consult.html\", clients=clients, message=message)","","if __name__ == \"__main__\":","    host = \"127.0.0.1\"","    port = \"8080\"","    app.run(host, port)"],"id":448},{"start":{"row":0,"column":0},"end":{"row":52,"column":23},"action":"insert","lines":["from flask import Flask, render_template, request","from database.db import *","from entities.client import Client","import html","","app = Flask(__name__)","","@app.route(\"/\")","def home():","    return render_template(\"home.html\")","    ","@app.route(\"/register_page\")","def register_page():","    return render_template(\"register.html\")","    ","@app.route(\"/register_user\", methods=[\"post\"])","def register_user():","    dni = request.form[\"dni\"]","    typeDocument = request.form[\"typeDocument\"]","    name = request.form[\"name\"]","    lastname = request.form[\"lastname\"]","    address = request.form[\"address\"]","    phoneNumber = request.form[\"phoneNumber\"]","    email = request.form[\"email\"]","    ","    try:","        save_client(client)","        message = \"Usuario registrado exitosamente\"","    except Error as e:","        message = f\"Fallo al registrar usuario: {e}\"","    ","    return redirect(url_for('list_clients', message=message))","    ","    ","@app.route(\"/clients\", methods=[\"GET\"])","def list_clients():","    clients = get_clients()","    print(clients)","    message = request.args.get('message')","    # Generar la tabla HTML","    tabla = \"<h1>Lista de Clientes</h1> <table border='1'><tr><th>ID</th><th>DNI</th><th>Tipo de Documento</th><th>Nombre</th><th>Apellido</th><th>Dirección</th><th>Número de Teléfono</th><th>Correo Electrónico</th></tr>\"","    for client in clients:","        tabla += f\"<tr><td>{client[0]}</td><td>{html.escape(client[1])}</td><td>{html.escape(client[2])}</td><td>{html.escape(client[3])}</td><td>{html.escape(client[4])}</td><td>{html.escape(client[5])}</td><td>{html.escape(client[6])}</td><td>{html.escape(client[7])}</td></tr>\"","","    tabla += \"</table>\"","","    return tabla","    #return render_template(\"consult.html\", clients=clients, message=message)","","if __name__ == \"__main__\":","    host = \"127.0.0.1\"","    port = \"8080\"","    app.run(host, port)"]}],[{"start":{"row":23,"column":33},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":449},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":83},"action":"insert","lines":["client = Client(dni, typeDocument, name, lastname, address, phoneNumber, email)"],"id":450}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":49},"action":"remove","lines":["from flask import Flask, render_template, request"],"id":452},{"start":{"row":0,"column":0},"end":{"row":0,"column":68},"action":"insert","lines":["from flask import Flask, request, redirect, url_for, render_template"]}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":77},"action":"remove","lines":["    #return render_template(\"consult.html\", clients=clients, message=message)"],"id":453},{"start":{"row":48,"column":16},"end":{"row":49,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":42,"column":13},"end":{"row":44,"column":13},"action":"insert","lines":["<script>","        alert(\"{{ message }}\");","    </script>"],"id":454}],[{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"remove","lines":["\""],"id":455}],[{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["'"],"id":456}],[{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"remove","lines":["\""],"id":457}],[{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":["'"],"id":458}],[{"start":{"row":44,"column":2},"end":{"row":44,"column":3},"action":"remove","lines":[" "],"id":459},{"start":{"row":44,"column":1},"end":{"row":44,"column":2},"action":"remove","lines":[" "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":1},"action":"remove","lines":[" "]},{"start":{"row":43,"column":31},"end":{"row":44,"column":0},"action":"remove","lines":["",""]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"remove","lines":[";"]}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":8},"action":"remove","lines":["    "],"id":460},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]},{"start":{"row":42,"column":21},"end":{"row":43,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":[" "],"id":461}],[{"start":{"row":42,"column":44},"end":{"row":42,"column":45},"action":"insert","lines":[";"],"id":462}],[{"start":{"row":42,"column":30},"end":{"row":42,"column":31},"action":"remove","lines":["{"],"id":463}],[{"start":{"row":42,"column":39},"end":{"row":42,"column":40},"action":"remove","lines":["}"],"id":464},{"start":{"row":42,"column":38},"end":{"row":42,"column":39},"action":"remove","lines":[" "]}],[{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"remove","lines":["'"],"id":465}],[{"start":{"row":42,"column":38},"end":{"row":42,"column":39},"action":"remove","lines":["'"],"id":466}],[{"start":{"row":42,"column":29},"end":{"row":42,"column":30},"action":"remove","lines":[" "],"id":467}],[{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"remove","lines":["="],"id":468},{"start":{"row":42,"column":10},"end":{"row":42,"column":15},"action":"insert","lines":["+= f\""]}],[{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"remove","lines":["\""],"id":469}],[{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"remove","lines":[" "],"id":470}],[{"start":{"row":41,"column":27},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":471},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]},{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["t"]},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["a"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["b"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["l"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["a"]}],[{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":[" "],"id":472},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":[" "],"id":473}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":14},"action":"insert","lines":["''"],"id":474}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":["'"],"id":475},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"remove","lines":["'"]}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":14},"action":"insert","lines":["\"\""],"id":476}],[{"start":{"row":40,"column":41},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":477},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":4},"end":{"row":41,"column":5},"action":"insert","lines":["p"]},{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["r"]},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["i"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["n"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":41,"column":9},"end":{"row":41,"column":11},"action":"insert","lines":["()"],"id":478}],[{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["m"],"id":479},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["e"]},{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["s"]},{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["s"]},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":["a"]},{"start":{"row":41,"column":15},"end":{"row":41,"column":16},"action":"insert","lines":["g"]},{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":18},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":480},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":20},"action":"insert","lines":["  print(message)"],"id":481}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"remove","lines":[" "],"id":482}],[{"start":{"row":42,"column":11},"end":{"row":42,"column":18},"action":"remove","lines":["message"],"id":483}],[{"start":{"row":42,"column":11},"end":{"row":42,"column":13},"action":"insert","lines":["\"\""],"id":484}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["h"],"id":485},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["o"]},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["l"]},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"remove","lines":[" "],"id":486}],[{"start":{"row":45,"column":51},"end":{"row":45,"column":52},"action":"insert","lines":[" "],"id":487}],[{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["\""],"id":488}],[{"start":{"row":45,"column":40},"end":{"row":45,"column":42},"action":"insert","lines":["\"\""],"id":489}],[{"start":{"row":45,"column":40},"end":{"row":45,"column":42},"action":"remove","lines":["\"\""],"id":490}],[{"start":{"row":45,"column":40},"end":{"row":45,"column":42},"action":"insert","lines":["\"\""],"id":491}],[{"start":{"row":45,"column":41},"end":{"row":45,"column":42},"action":"remove","lines":["\""],"id":492}],[{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"remove","lines":["\""],"id":493}],[{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["'"],"id":494}],[{"start":{"row":45,"column":40},"end":{"row":45,"column":41},"action":"remove","lines":["\""],"id":495}],[{"start":{"row":45,"column":40},"end":{"row":45,"column":42},"action":"insert","lines":["''"],"id":496}],[{"start":{"row":45,"column":41},"end":{"row":45,"column":42},"action":"remove","lines":["'"],"id":497}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":26},"action":"remove","lines":["Usuario"],"id":498},{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["C"]},{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["l"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["i"]},{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["e"]},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["n"]},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["t"]},{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":39},"end":{"row":31,"column":46},"action":"remove","lines":["usuario"],"id":499},{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":["c"]},{"start":{"row":31,"column":40},"end":{"row":31,"column":41},"action":"insert","lines":["l"]},{"start":{"row":31,"column":41},"end":{"row":31,"column":42},"action":"insert","lines":["i"]},{"start":{"row":31,"column":42},"end":{"row":31,"column":43},"action":"insert","lines":["e"]},{"start":{"row":31,"column":43},"end":{"row":31,"column":44},"action":"insert","lines":["n"]},{"start":{"row":31,"column":44},"end":{"row":31,"column":45},"action":"insert","lines":["t"]},{"start":{"row":31,"column":45},"end":{"row":31,"column":46},"action":"insert","lines":["e"]}],[{"start":{"row":42,"column":3},"end":{"row":42,"column":17},"action":"remove","lines":[" print(\"hola\")"],"id":500},{"start":{"row":42,"column":2},"end":{"row":42,"column":3},"action":"remove","lines":[" "]},{"start":{"row":42,"column":1},"end":{"row":42,"column":2},"action":"remove","lines":[" "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":1},"action":"remove","lines":[" "]},{"start":{"row":41,"column":18},"end":{"row":42,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":43,"column":14},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":501},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":44,"column":5},"action":"insert","lines":["i"]},{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":[" "],"id":502},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["m"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["e"]},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["s"]},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["s"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["a"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["g"]},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":[" "],"id":503}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":15},"action":"remove","lines":["if message "],"id":504},{"start":{"row":44,"column":4},"end":{"row":45,"column":33},"action":"insert","lines":["if len(my_string) == 0:","    print(\"La cadena está vacía\")"]}],[{"start":{"row":45,"column":33},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":505},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":11},"end":{"row":44,"column":20},"action":"remove","lines":["my_string"],"id":506},{"start":{"row":44,"column":11},"end":{"row":44,"column":18},"action":"insert","lines":["message"]}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":22},"action":"remove","lines":["=="],"id":507},{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["<"]}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"remove","lines":["<"],"id":508}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":[">"],"id":509}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "],"id":510}],[{"start":{"row":45,"column":8},"end":{"row":45,"column":37},"action":"remove","lines":["print(\"La cadena está vacía\")"],"id":511},{"start":{"row":45,"column":8},"end":{"row":45,"column":57},"action":"insert","lines":["tabla += f\"<script> alert('{message}'); </script>"]}],[{"start":{"row":45,"column":57},"end":{"row":45,"column":58},"action":"insert","lines":["\""],"id":512}],[{"start":{"row":47,"column":15},"end":{"row":47,"column":53},"action":"remove","lines":["<script> alert('{message}'); </script>"],"id":513}],[{"start":{"row":47,"column":15},"end":{"row":47,"column":16},"action":"remove","lines":[" "],"id":514}],[{"start":{"row":44,"column":7},"end":{"row":44,"column":24},"action":"remove","lines":["len(message) > 0:"],"id":515},{"start":{"row":44,"column":7},"end":{"row":44,"column":25},"action":"insert","lines":["my_string is None:"]}],[{"start":{"row":44,"column":7},"end":{"row":44,"column":25},"action":"remove","lines":["my_string is None:"],"id":516},{"start":{"row":44,"column":7},"end":{"row":44,"column":29},"action":"insert","lines":["my_string is not None:"]}],[{"start":{"row":44,"column":7},"end":{"row":44,"column":16},"action":"remove","lines":["my_string"],"id":517},{"start":{"row":44,"column":7},"end":{"row":44,"column":14},"action":"insert","lines":["message"]}],[{"start":{"row":23,"column":33},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":518},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["l"],"id":519},{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"insert","lines":["e"]},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["n"]},{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["g"]},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["u"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["a"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"remove","lines":["e"],"id":520}],[{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["j"],"id":521},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["e"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":[" "],"id":522},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":[" "],"id":523},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["r"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["e"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["q"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["u"]},{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["e"]},{"start":{"row":24,"column":21},"end":{"row":24,"column":22},"action":"insert","lines":["s"]},{"start":{"row":24,"column":22},"end":{"row":24,"column":23},"action":"insert","lines":["t"]},{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["."]},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["f"]}],[{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["o"],"id":524},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["r"]},{"start":{"row":24,"column":27},"end":{"row":24,"column":28},"action":"insert","lines":["m"]}],[{"start":{"row":24,"column":28},"end":{"row":24,"column":30},"action":"insert","lines":["[]"],"id":525}],[{"start":{"row":24,"column":29},"end":{"row":24,"column":31},"action":"insert","lines":["\"\""],"id":526}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":39},"action":"insert","lines":["lenguajes"],"id":527}],[{"start":{"row":24,"column":41},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":528},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["p"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["r"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["i"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["n"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"remove","lines":["t"],"id":529},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"remove","lines":["n"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"remove","lines":["i"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["r"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["r"],"id":530},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["e"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["t"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["u"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["r"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":[" "],"id":531},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["l"]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["e"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["n"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["g"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["u"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["a"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["j"]},{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":["e"]},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":20},"action":"remove","lines":["    return lenguajes"],"id":532}],[{"start":{"row":24,"column":2},"end":{"row":24,"column":41},"action":"remove","lines":["  lenguajes = request.form[\"lenguajes\"]"],"id":533},{"start":{"row":24,"column":1},"end":{"row":24,"column":2},"action":"remove","lines":[" "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["",""],"id":534},{"start":{"row":23,"column":33},"end":{"row":24,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":133.33333686546052,"scrollleft":0,"selection":{"start":{"row":23,"column":33},"end":{"row":23,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1718677976752,"hash":"4c8fb97939caaa68ca835a1f5d88e452267ec054"}