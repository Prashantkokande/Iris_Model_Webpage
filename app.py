from flask import Flask, render_template, request
import pickle
import numpy as np

# Load your trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs from the form
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    
    # Prepare input data for prediction
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Predict the class
    prediction = model.predict(input_data)
    
    # Map prediction to flower name
    species = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
    result = species[prediction[0]]
    
    return render_template('index.html', prediction_text=f'The predicted species is {result}')

if __name__ == "__main__":
    app.run(debug=True)
