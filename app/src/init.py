from flask import Flask

from .services.initializer_service import InitializerService
from .views.handlers.errors import errors
from .views.controller import controller
from flasgger import Swagger

app = Flask(__name__)
app.config["SWAGGER"] = {"openapi": "3.0.2"}
swagger = Swagger(app, template_file="./swagger/openapi.yml")

app.register_blueprint(blueprint=controller, url_prefix="/filmbuddy/v1/")
app.register_blueprint(blueprint=errors, url_prefix="/filmbuddy/v1/")

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
