from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

from routes.route import *

if __name__ == "__main__":
    host = "0.0.0.0"
    port = "80"
    app.run(host, port)