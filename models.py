from app import db

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)
    image_url = db.Column(db.Text)

    def __init__(self, name, price, image_url):
        self.name = name
        self.price = price
        self.image_url = image_url
