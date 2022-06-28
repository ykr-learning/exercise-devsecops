"""
This file runs the Flask application we are using as an API endpoint.
"""

import pickle
 
from flask import Flask
from flask import request
from flask import jsonify
import json
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn import preprocessing
import numpy as np
import pandas as pd
# Create a flask
app = Flask(__name__)
class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
# Load pickled model file
model = joblib.load('chrunlog_r.pkl')
y=np.array([0,1])
@app.route("/")
def hello():
    print("Handling request to home page.")
    return "Hello, Azure!"
# Create an API end point
@app.route('/api/v1.0/predict', methods=['GET'])
def get_prediction(trained_model=model):
    #  ['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip'] 
    # tenure
    tenure = float(request.args.get('tenure'))
    # age
    age = float(request.args.get('age'))
    # address
    address = float(request.args.get('address'))
    #income
    income = float(request.args.get('income'))
	#ed
    ed = float(request.args.get('ed'))
	#employ
    employ = float(request.args.get('employ'))
	#equip
    equip = float(request.args.get('equip'))
    # The features of the observation to predict
    data_features=pd.DataFrame([tenure, age, address, income, ed, employ, equip])
    features = np.asarray(data_features).reshape(1, -1) 
    features = preprocessing.StandardScaler().fit(features).transform(features)
    # Predict the class using the model
    predicted_class = int(trained_model.predict(features.reshape(1, -1) ))
 
    # Return a json object containing the features and prediction
    return jsonify(features=json.dumps(data_features.to_json(), cls=NumpyEncoder), predicted_class=json.dumps( predicted_class, cls=NumpyEncoder))

if __name__ == '__main__':
    # Run the app at 0.0.0.0:3333
    app.run(port=80,host='0.0.0.0')
