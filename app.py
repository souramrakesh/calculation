from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np

app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template("index1.html")
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        first_number = request.form['Please Enter the first Number']
        second_number = request.form['Please Enter the second Number']
        if first_number and second_number in "1234567890":
            predict = (int(first_number)+int(second_number))
            return render_template('templates/index1.html', text ="Addition of {} and {} is :{}".format(first_number,second_number,predict))
        else:
            return render_template('templates/index1.html',text ="Please Enter an integer")

if __name__=="__main__":
    app.run(debug=True)


