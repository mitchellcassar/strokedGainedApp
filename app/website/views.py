from flask import Blueprint, render_template, request
import pandas as pd
from .logic import Shot
from .references import comparisonBaseline, shotCategory

data = pd.read_csv('website/dataset.csv')

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@views.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        shotData = dict(request.form)    
        shot = Shot(shotData['startDistance'],shotData['startLie'],shotData['finishDistance'],shotData['finishLie'],shotData['baseline'])
        
        if shot.shotNotValid():
            return render_template('invalid.html')
        
        dataToRender = (
            shot.calcShotValue(data),
            comparisonBaseline[shot.baseline],
            shotCategory[shot.lookupShot(data, code = str(shot.startDistance) + shot.startLie, lookupColumn='sgCategory')]
        )
    
    return render_template('results.html', dataToRender = dataToRender) 

