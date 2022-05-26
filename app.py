from crypt import methods
import pandas as pd
import numpy as np
from requests import request
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request
from flask_restx import Api, Resource
import joblib
import json
import pickle as pic

clf5_from_joblib = joblib.load('5_model2.pkl')

clf4_from_joblib = joblib.load('4_model2.pkl')

clf2_from_joblib = joblib.load('testmodel.pkl')

app = Flask(__name__)
api = Api(app)

@api.route('/quest')
class HelloWorld(Resource):
    def post(self):
        content = request.get_json()

        print(content)

        data = pd.read_json(json.dumps(content))

        Floor = data.Floor

        Floor = Floor[0]

        macs = data.macs
        X = []
        for a in macs:
            X.append(a)
        x = []
        x.append(X)
        X = pd.DataFrame(x)

        if Floor == 2:
            result = str(clf2_from_joblib.predict(X))
        elif Floor == 4:
            result = str(clf4_from_joblib.predict(X))
        elif Floor == 5:
            result = str(clf5_from_joblib.predict(X))

        return {"Result":result}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)


