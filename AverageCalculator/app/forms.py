from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NumberForm(FlaskForm):
    numbers = StringField("Enter numbers (comma separated):", validators=[DataRequired()])
    submit = SubmitField("Calculate Average")
