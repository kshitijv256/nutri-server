import os
from flask import Flask, flash, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename

import pandas as pd 
import matplotlib.pyplot as plt
import csv 
from urllib.parse import urlparse
from urllib.parse import parse_qs


data = pd.read_csv("food_db (1).csv")
# data.fillna(0, inplace=True, axis=1)
# data.to_csv("food_db (1).csv", index=False)
print(data.shape)

def processing(map_data):
    pass

def select(query):
    # query = query.upper
    data2 = data.query(' Category == @query')
    data2 = data2.sort_values('score',ascending=False)
    return data2.set_index('ID').to_dict('list')
print(select("BUTTER"))

app = Flask(__name__)
app.secret_key = 'super_secret'

@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify("It is working!")

@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.args:
        q = request.values.get('details')
        res = select(q)
        # query = query.upper
        # data1 = data.query(' "Category" == @query')
        return jsonify(res)
        # return "Hello, {}".format(request.data)
    else:
        return jsonify({"category":"error", "details":"No data found"})


if __name__ == "__main__":
    app.run(host='0.0.0.0')