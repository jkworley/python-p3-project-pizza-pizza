from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Menu(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String)
    price = db.Column(db.Float)
    picture = db.Column(db.String)
    

    order_items= db.relationship('Order', backref = 'menu')




class Customer(db.Model):

    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email_address = db.Column(db.String)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.Integer)

    customer_orders = db.relationship('Order', backref = 'customer')




class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True)

    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    order_item = db.Column(db.Integer, db.ForeignKey('items.id'))
    created_at = db.Column(db.Float)
    # order_total = db.Column(db.String) not sure if we need ..
    
