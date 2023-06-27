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
                item_name = "Plain Pizza",
                price = 3.00,
                description= "Mmm plain pizza."
            ), 
            Menu (
                item_name = "Pepperoni Pizza",
                price = 3.50,
                description= "Plain pizza with pepperoni on top."
            ),
            Menu (
                item_name = "Veggie Pizza",
                price = 3.75,
                description= "Plain pizza with veggies on top."
            ),
            Menu (
                item_name = "Supreme Pizza",
                price = 3.75,
                description= "Plain pizza with pepperoni, sausage, mushrooms, peppers, red onions, cheese."
            ),
            Menu (
                item_name = "Margherita Pizza",
                price = 3.90,
                description= "Plain pizza with fresh mozzarella topped with the farm fresh tomatoes and fresh basil."
            ),
            Menu (
                item_name = "BBQ Chicken",
                price = 4.05,
                description= "Plain pizza with BBQ Chicken."
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



        # commit CREATE - UPDATE - DELETE actions
        db.session.commit()

        # for i in Menu.query.all():
        #     print(i.description)