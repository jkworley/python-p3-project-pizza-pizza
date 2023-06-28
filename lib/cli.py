from app import app # required if using Flask-SQLAlchemy

from models import db, Menu,Order,Customer

import time

if __name__ == '__main__':
    with app.app_context(): # required if using Flask-SQLAlchemy

        print("\nWelcome to Pizza Pizza!\n")

        new_order = []

        while True:
            answer = input("Have you ordered from us before? (Y/N) ")
            
            if answer.lower() not in ["yes", "y"]: # if answer is "N"
                print ("\nPlease provide your information: \n") 
                
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                email_address = input("Email: ")
                street_address = input("Street Address: ")
                city = input("City: ")
                state = input("State: ")
                zip_code = input("Zip Code: ")
                
                new_customer = Customer (
                    first_name = first_name,
                    last_name = last_name,
                    email_address = email_address,
                    street_address = street_address,
                    city = city,
                    state = state,
                    zip_code = zip_code
                )

                db.session.add(new_customer)

                db.session.commit()

                new_order.append(new_customer.id)

                print(f"\nThanks for ordering from Pizza Pizza, {new_customer.first_name.title()}!\n")

                break

            else: # if answer is "Y"
                while True:
                    search_term = input("\nPlease enter your email address: ") 
                    customer = Customer.query.filter(Customer.email_address == search_term).first()

                    if customer:
                        answer = input(f"\nAre you {customer.first_name} {customer.last_name}? (Y/N) ")

                        if answer.lower() not in ["yes", "y"]: # if answer is "N"
                            print ("\nPlease provide your information: \n") 
                
                            first_name = input("First Name: ")
                            last_name = input("Last Name: ")
                            email_address = input("Email: ")
                            street_address = input("Street Address: ")
                            city = input("City: ")
                            state = input("State: ")
                            zip_code = input("Zip Code: ")
                            
                            new_customer = Customer (
                                first_name = first_name,
                                last_name = last_name,
                                email_address = email_address,
                                street_address = street_address,
                                city = city,
                                state = state,
                                zip_code = zip_code
                            )

                            db.session.add(new_customer)

                            db.session.commit()

                            new_order.append(new_customer.id)

                            print(f"\nThanks for ordering from Pizza Pizza, {new_customer.first_name.title()}!")
                            print(f"\nNow your information is saved for next time!")

                            break
                        
                        else: # if answer is "Y"
                            new_order.append(customer.id)

                            print(f"\nGood to see you again, {customer.first_name.title()}!")

                            break

                    else:
                        print("\nCustomer not found...")

                break
       
        # first gather customer info 
        # create customer object based on inputed info 
        # ask to see menu y/n
        # show menu (maybe in table format with all of the information?)
        # select from menu 
        # create a order object (will join customer ID with the menu ID)
        # maybe have a time lapse 
        # show receipt of item
        # could also add a repetive loop to send it back to the top 

        print(new_order)

        print("\nTake a look at our menu: \n")

        for i in Menu.query.all():
            print(f"{i.item_name} - ${i.price}")
            print(f"{i.description}\n")

        user_order = input("\nWhat would you like to order? ")