from flask import Flask

from .views.controller import controller

app = Flask(__name__)

app.register_blueprint(blueprint=controller)


@app.route('/')
def index():
    return "Home"



