from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Define the Flask application
app = Flask(__name__)

# Load the machine learning model
model = pickle.load(open('active.pkl', 'rb'))

# Define API endpoints


@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    query = pd.get_dummies(query_df)
    predictiond = model.predict(query)
    return jsonify({'predictiond': predictiond.tolist()})


# Run the Flask application
if __name__ == '__main__':
    app.run(port=5000, debug=True)
