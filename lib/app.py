from flask import Flask
from flask_migrate import Migrate

from models import db

app = Flask(__name__) # establishes DB connection

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza_pizza.db" # sets DB URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app) # initializes DB

if __name__ == "__main__":
    app.run(port = 5555, debug = True) # chooses port on which to open app