from flask import Flask
from config import Config
# Lowercase for the file/package
# Uppercases for Class

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
