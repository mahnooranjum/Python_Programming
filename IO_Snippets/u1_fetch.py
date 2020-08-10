'''
    Author: Mahnoor Anjum
    Fetch data
'''

import pandas as pd 
import flask 

n1 = r'data/10r.csv'
n2 = r'data/1000r.csv'
c = 'SEQNO'

def saver(dataframe, fname):
    dataframe.to_json(fname+'.json')

def fetch_saver(n1, n2, var):
    f1 = pd.read_csv(n1)[var]
    f2 = pd.read_csv(n2)[var]
    saver(f1, n1.split('.')[0]+'_'+var)
    saver(f2, n2.split('.')[0]+'_'+var)
    return


fetch_saver(n1, n2, c)
    

    