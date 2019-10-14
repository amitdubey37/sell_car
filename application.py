import os
from flask import Flask, jsonify, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddCarForm, DeleteCarForm
from werkzeug.utils import secure_filename
# from models import Car

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

image_dir = basedir + "/static/images"

app.config['SECRET_KEY'] = 'mysupersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:puri_sabji37@database-1.cpeisv2u7g6m.us-east-2.rds.amazonaws.com/cars'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


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



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    form = AddCarForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        image = form.image.data
        file_name = secure_filename(image.filename)
        file_path = os.path.join(image_dir, file_name)
        image.save(file_path)
        car = Car(name, price, os.path.join("/static/images",file_name))
        db.session.add(car)
        db.session.commit()
        flash("Car {} added successfully!".format(name))
        redirect(url_for('list_car'))
    return render_template('add_car.html', form=form)

@app.route('/list_car')
def list_car():
    cars = Car.query.all()
    return render_template('list_car.html', cars=cars)

@app.route('/delete', methods=["GET", "POST"])
def delete():
    form = DeleteCarForm()
    if form.validate_on_submit():
        car = Car.query.get(form.id.data)
        db.session.delete(car)
        db.session.commit()
        flash("{} Deleted!".format(car.name))
        redirect(url_for('list_car'))
    return render_template('delete.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
