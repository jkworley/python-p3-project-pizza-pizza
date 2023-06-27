from app import app # required if using Flask-SQLAlchemy
from models import db, Menu, Order, Customer


if __name__ == '__main__':
    with app.app_context():

        Menu.query.delete()
        Order.query.delete()
        Customer.query.delete()

        items = [
            Menu (
                item_name = "Pizza",
                price = 3.00,
                picture= "https://www.foodandwine.com/thmb/Wd4lBRZz3X_8qBr69UOu2m7I2iw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-cheese-pizza-FT-RECIPE0422-31a2c938fc2546c9a07b7011658cfd05.jpg",
                
            ) #needs comma here 
            # Menu (
            #     name = "Millie",
            #     species = "cat",
            #     breed = "maine coon",
            #     temperament = "charming"
            # ),
            # Menu (
            #     name = "Dave",
            #     species = "cow",
            #     breed = "Gurnsey",
            #     temperament = "happy"
            # )
        ]

        # add objects to db
        db.session.add_all(items)

        


        # customers = [
        #     Customer (
        #         person_id = 1,
        #         pet_id = 1
        #     ),
        #     Customer (
        #         person_id = 1,
        #         pet_id = 2
        #     ),
        #     Customer (
        #         person_id = 2,
        #         pet_id = 3
        #     )
        # ]

        # db.session.add_all(customers)

        # commit CREATE - UPDATE - DELETE actions
        db.session.commit()