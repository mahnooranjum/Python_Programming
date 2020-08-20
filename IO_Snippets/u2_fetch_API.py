'''
    Author: Mahnoor Anjum
    Fetch data
'''

import pandas as pd 
import flask 


def saver(dataframe, fname):
    dataframe.to_json(fname+'.json')

def fetch_saver(n1, n2, var):
    f1 = pd.read_csv(n1)[var]
    f2 = pd.read_csv(n2)[var]
    saver(f1, n1.split('.')[0]+'_'+var)
    saver(f2, n2.split('.')[0]+'_'+var)
    return



from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    n1 = None
    n2 = None
    c = None
    if request.method == 'POST' and\
          ('n1' in request.form)and \
            ('n2' in request.form)and\
              ('c' in request.form):
                  
        n1 = request.form['n1']
        n2 = request.form['n2']
        c = request.form['c']

        fetch_saver(n2, n1, c)

       
    return render_template('index.html')

app.run(port=5000)

