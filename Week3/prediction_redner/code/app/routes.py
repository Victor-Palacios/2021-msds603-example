from app import application, classes, model
from flask import render_template, redirect, url_for

@application.route('/index', methods=('GET','POST'))
@application.route('/', methods=('GET','POST'))
def index():
    input_form = classes.InputForm()
    if input_form.validate_on_submit():
        sep_len = float(input_form.sep_len.data)
        sep_wid = float(input_form.sep_wid.data)
        pet_len = float(input_form.pet_len.data)
        pet_wid = float(input_form.pet_wid.data)
        prediction = model.predict_data(sep_len, sep_wid, pet_len, pet_wid)
        return render_template('prediction.html', output=int(prediction))
    return render_template('index.html', form=input_form)
