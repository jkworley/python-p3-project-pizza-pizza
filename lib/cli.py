from app import app # required if using Flask-SQLAlchemy

from models import db, Menu,Order,Customer

import time

from sqlalchemy import select,func

from art import *

if __name__ == '__main__':
    with app.app_context(): # required if using Flask-SQLAlchemy
        art = text2art("\nWelcome   to \nPIZZA PIZZA")
        print(art)
        
        new_order = []

        while True:
            answer = input("Have you ordered from us before? (Y/N) ")
            
            if answer.lower() not in ["yes", "y"]: # if answer is "N"
                print ("\nPlease provide your information: \n") 
                
                first_name = input("First Name: ").strip()
                last_name = input("Last Name: ").strip()
                email_address = input("Email: ").strip()
                street_address = input("Street Address: ").strip()
                city = input("City: ").strip()
                state = input("State: ").strip()
                zip_code = input("Zip Code: ").strip()
                
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
                    search_term = input("\nPlease enter your email address:").strip()
                    customer = Customer.query.filter(Customer.email_address == search_term).first()

                    if customer:
                        answer = input(f"\nAre you {customer.first_name} {customer.last_name}? (Y/N) ").strip()

                        if answer.lower() not in ["yes", "y"]: # if answer is "N"
                            print ("\nPlease provide your information: \n") 
                
                            first_name = input("First Name: ").strip()
                            last_name = input("Last Name: ").strip()
                            email_address = input("Email: ").strip()
                            street_address = input("Street Address: ").strip()
                            city = input("City: ").strip()
                            state = input("State: ").strip()
                            zip_code = input("Zip Code: ").strip()
                            
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

                        else:
                            new_order.append(customer.id)
                            print(f"\nGood to see you again, {customer.first_name.title()}!")

                            break
                     
                    else:
                        print("\nCustomer not found...")

                break

        print("\nTake a look at our menu: \n")

        for i in Menu.query.all():
            print(f"{i.item_name} - ${i.price}")
            print(f"{i.description}\n")

        user_order = input("\nWhat would you like to order? ").strip()
       
        while True:
            
            menu_item = Menu.query.filter(func.lower(Menu.item_name) == func.lower(user_order)).first()
            
            if menu_item:
                
                customer_order = Order (
                    user_id = new_order[0],
                    order_item = menu_item.id,
                    created_at = time.time(),
                )
                
                db.session.add(customer_order)

                db.session.commit()

                print (f"\nYour order for {menu_item.item_name} has been placed!\n") 

                print(f"\nYour total amount due today is ${menu_item.price}.\n")

                print(f"\nHang tight while we get your {menu_item.item_name} ready! Your wait time is 5 minutes...\n")

                time.sleep(10)

                order_name = Customer.query.filter(Customer.id == new_order[0]).first()

                print(f"\n{order_name.first_name}, your order is up! The kitchen was moving fast today!\n")

                time.sleep(3)

                print(("""\
                                     ._
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.  `\`
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','       :
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
    i'
    :
                """))

                break
