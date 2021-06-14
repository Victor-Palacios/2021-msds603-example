from flask import Flask
from config import Config

# Initialization
# Create an application instance (an object of class Flask)  which handles all requests.
application = Flask(__name__)
application.config.from_object(Config)


# Added at the bottom to avoid circular dependencies. (Altough it violates PEP8 standards)
from app import classes
from app import routes



