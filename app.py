from flask import Flask, request, jsonify, render_template , joblib
#import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


app = Flask(__name__)



# Load model if exists, otherwise train
try:
    model = joblib.load('model.pkl')
    # Load iris for target_names
    iris = load_iris()
except FileNotFoundError:  # Specific exception instead of bare except
    # Train model
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    # Save model
    joblib.dump(model, 'model.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({
        'prediction': int(prediction[0]),
        'class': iris.target_names[prediction[0]]
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
