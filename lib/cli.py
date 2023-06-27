from app import app # required if using Flask-SQLAlchemy

from models import db, Menu,Order,Customer

import time

if __name__ == '__main__':
    with app.app_context(): # required if using Flask-SQLAlchemy

        print("Welcome to my app!")