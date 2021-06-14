from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    sep_len = StringField('Sepal Length:', validators=[DataRequired()])
    sep_wid = StringField('Sepal Width:', validators=[DataRequired()])
    pet_len = StringField('Petal Length:', validators=[DataRequired()])
    pet_wid = StringField('Petal Width:', validators=[DataRequired()])
    submit = SubmitField('Submit')


