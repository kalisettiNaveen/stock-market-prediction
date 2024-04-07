from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from random import *

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def main():
    return render_template('form.html')



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['Open']

    arr = np.array([val1])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])
    result_string = "The Stocks close value is around: " + str(pred)

    return render_template('form.html', pred=result_string)


#if __name__ == '__main__':
    #app.run(debug=True)