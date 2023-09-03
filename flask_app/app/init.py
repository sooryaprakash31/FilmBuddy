from flask import Flask

from .views.handlers.errors import errors
from .views.controller import controller

app = Flask(__name__)

app.register_blueprint(blueprint=controller)
app.register_blueprint(blueprint=errors)

@app.route('/')
def index():
    return "Hi, I am your FilmBuddy. Use /recommend for film recommendations"



