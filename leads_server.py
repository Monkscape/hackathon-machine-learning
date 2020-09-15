import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask('leads')

with open('leads-model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

def predict_prospects(prospects, dv, model):
    X = dv.transform(prospects)
    y_pred = model.predict_proba(X)[:,1]
    return y_pred

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG'

@app.route('/predict', methods=['POST'])
def predict():
    prospects = request.get_json()
 
    predictions = predict_prospects(prospects, dv, model)
    
    prediction_results = []
    for prediction in predictions:
        prediction_results.append({
            'lead_probability': float(prediction),
            'conversion': bool(prediction >= 0.5),
        })

    return jsonify(prediction_results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)