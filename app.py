from flask import Flask, request, redirect, jsonify, render_template, url_for
# import pymongo
import pandas as pd
import numpy as np
import sklearn
from utils import FISH_WEIGHT
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Fish Weight Prediction")
    return render_template("index.html")



@app.route('/predict_fish_weight', methods = ['GET', 'Post'])
def predict_fish_weight():

    if request.method == 'POST':
        data = request.form
    
        Species = request.form['Species']
        Length1 = eval(request.form['Length1'])
        Length2 = eval(request.form['Length2'])
        Length3 = eval(request.form['Length3'])
        Height = eval(request.form['Height'])
        Width = eval(request.form['Width'])

        fish_weight = FISH_WEIGHT(data)
        predict_weight = fish_weight.get_fish_weight()

        if predict_weight < 0:
            predict_weight = 'Invalid inputs, Please try again.'

        data = dict(data)
        # data["Predicted_weight"] = predict_weight
        print(data)
        # fish_weight.collection_user.insert_one(data)

        # return jsonify({"predicted weight" :predict_weight})

        return render_template("index.html", prediction_text = predict_weight)

    else:
        data = request.form
        # print("data :", data)

        Species = request.form['Species']
        Length1 = eval(request.form['Length1'])
        Length2 = eval(request.form['Length2'])
        Length3 = eval(request.form['Length3'])
        Height = eval(request.form['Height'])
        Width = eval(request.form['Width'])

        fish_weight = FISH_WEIGHT(data)
        predict_weight = fish_weight.get_fish_weight()

        if predict_weight < 0:
            predict_weight = 'Invalid inputs, Please try again.'

        data = dict(data)
        # data["Predicted_weight"] = predict_weight
        print(data)
        # fish_weight.collection_user.insert_one(data)

        # return jsonify({"predicted weight" :predict_weight})
        return render_template("index.html", prediction_text = predict_weight)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= config.PORT_NUMBER)

