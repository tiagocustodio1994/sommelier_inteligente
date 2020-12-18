import joblib
import os

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUlj5oI1c'

bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    alcohol = FloatField('Alcohol: ', validators=[DataRequired()])
    malic_acid = FloatField('Malic Acid: ', validators=[DataRequired()])
    ash = FloatField('Ash: ', validators=[DataRequired()])
    alcalinity = FloatField('Alcalinity of Ash: ', validators=[DataRequired()])
    magnesium = FloatField('Magnesium: ', validators=[DataRequired()])
    phenols = FloatField('Total Phenols: ', validators=[DataRequired()])
    flavanoids = FloatField('Flavanoids: ', validators=[DataRequired()])
    nonflavanoid = FloatField('Nonflavanoid Phenols: ', validators=[DataRequired()])
    proanthocyanins = FloatField('Proanthocyanins: ', validators=[DataRequired()])
    color = FloatField('Color Intensity: ', validators=[DataRequired()])
    hue = FloatField('Hue: ', validators=[DataRequired()])
    diluted = FloatField('OD280/OD315 of diluted wines: ',validators=[DataRequired()])
    proline = FloatField('Proline: ', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    classe = 'no-image'
    if form.validate_on_submit():
        x = [[form.alcohol.data, form.malic_acid.data, form.ash.data, form.alcalinity.data, form.magnesium.data,
        form.phenols.data, form.flavanoids.data, form.nonflavanoid.data, form.proanthocyanins.data,
        form.color.data, form.hue.data, form.diluted.data, form.proline.data]]
        classe = make_prediction(x)
    return render_template('index.html', form=form, classe=classe)

def make_prediction(x):
    filename = os.path.join('app','model','finalized_model.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]