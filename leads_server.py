import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask('leads')

with open('leads-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

def predict_single(prospect, dv, model):
    X = dv.transform([prospect])
    y_pred = model.predict_proba(X)[:,1]
    return y_pred[0]

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG'

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
 
    prediction = predict_single(customer, dv, model)
    conversion = prediction >= 0.5
    
    result = {
        'lead_probability': float(prediction),
        'conversion': bool(conversion),
    }
 
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)