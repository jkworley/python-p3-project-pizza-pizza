from app import app # required if using Flask-SQLAlchemy

from models import db, Menu,Order,Customer

import time

if __name__ == '__main__':
    with app.app_context(): # required if using Flask-SQLAlchemy

        print("Welcome to my app!")
       
        # first gather customer info 
        #create customer object based on inputed info 
        # Ask to see menu y/n
        # show menu (maybe in table format with all of the information?)
        #select from menu 
        #create a order object (will join customer ID with the menu ID)
        # maybe have a time lapse 
        # show receipt of item
        # could also add a repetive loop to send it back to the top 






        
        for i in Menu.query.all():
             print(i.item_name)

        input("What would you like to order? ")

        