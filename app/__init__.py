from flask import Flask
from config import Config #config = module config.py ; Config = actual class in the config.py file

app = Flask(__name__)
app.config.from_object(Config)

from app import routes