from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField, FileRequired


class AddCarForm(FlaskForm):
    name = StringField('Enter car name')
    price = StringField('Enter car price')
    image = FileField('Upload file', validators=[FileRequired()])
    submit = SubmitField("Add Car")


class DeleteCarForm(FlaskForm):
    id = IntegerField('Enter car id to delete')
    submit = SubmitField("Delete Car")
