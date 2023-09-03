from flask import Flask

from .services.initializer_service import InitializerService
from .views.handlers.errors import errors
from .views.controller import controller

app = Flask(__name__)

app.register_blueprint(blueprint=controller)
app.register_blueprint(blueprint=errors)

initializer = InitializerService()
initialized = False


def perform_initialization():
    global initialized
    if not initialized:
        initializer.initialize()
        initialized = True


perform_initialization()


@app.route('/')
def index():
    return "Hi, I am your FilmBuddy. Use /recommend for film recommendations"
