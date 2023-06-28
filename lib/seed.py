from app import app # required if using Flask-SQLAlchemy
from models import db, Menu, Order, Customer

from faker import Faker

fake = Faker()


if __name__ == '__main__':
    with app.app_context():

        Menu.query.delete()
        Order.query.delete()
        Customer.query.delete()

        items = [
            Menu (
                item_name = "Mozzarella Pizza",
                price = 3.15,
                description= "This pizza will satisfy even the pickiest tastebuds....Mmmmm plain pizza."
            ), 
            Menu (
                item_name = "Pepperoni Pizza",
                price = 3.45,
                description= "Our classic plain pizza topped with the finest imported pepperoni's on the market."
            ),
            Menu (
                item_name = "Veggie Pizza",
                price = 3.75,
                description= "For our veggie lovers out there! This pizza is topped with five different vegetables! Hand picked each week from our local Farmers Market;."
            ),
            Menu (
                item_name = "Supreme Pizza",
                price = 4.75,
                description= " A good choice for the carnivore in the room! This pizza is loaded with pepperoni, sausage, mushrooms, peppers, red onions and cheese."
            ),
            Menu (
                item_name = "Margherita Pizza",
                price = 3.99,
                description= "This pizza gets our special in house rosemary crust topped with mozzarella, thinly sliced heirloom tomatoes and fresh basil."
            ),
            Menu (
                item_name = "BBQ Chicken",
                price = 4.55,
                description= "The world has been waiting for this pizza.... Slow marinated BBQ chicken atop a bed of melted mozzarella!"
            )
        ]

        # add objects to db
        db.session.add_all(items)

        
        customer = []

        for i in range (5):
            fake_customer = Customer (
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email_address = fake.email(),
                street_address = fake.street_address(),
                city = fake.city(),
                state = fake.state(),
                zip_code = fake.postcode()
            )
            

            customer.append(fake_customer)

        db.session.add_all(customer)



        
        db.session.commit()

     