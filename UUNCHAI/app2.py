from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the fertilizer recommendation model
fertilizer_model = pickle.load(open('stored_model_fr.pkl', 'rb'))  # Ensure the filename is correct

# Encoders for the categorical variables
soil_type_encoder = LabelEncoder()
crop_type_encoder = LabelEncoder()

# Fit the encoders with the categories present in the dataset
soil_types = ['Sandy', 'Loamy', 'Black', 'Red', 'Clayey']
crop_types = ['Maize', 'Sugarcane', 'Cotton', 'Tobacco', 'Paddy', 'Barley', 'Wheat', 'Millets', 'Oil seeds', 'Pulses', 'Ground Nuts']

soil_type_encoder.fit(soil_types)
crop_type_encoder.fit(crop_types)

@app.route('/')
def fertilizer_page():
    return render_template('page2.html')

@app.route('/predict_fertilizer', methods=['POST'])
def predict_fertilizer():
    # Extract form values
    form_values = request.form.to_dict()
    
    # Convert form values to appropriate data types
    int_features = [
        float(form_values['temperature']),
        float(form_values['humidity']),
        float(form_values['moisture']),
        soil_type_encoder.transform([form_values['soil_type']])[0],
        crop_type_encoder.transform([form_values['crop_type']])[0],
        float(form_values['nitrogen']),
        float(form_values['potassium']),
        float(form_values['phosphorous']),
    ]
    
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = fertilizer_model.predict(final)
    output = f"The recommended fertilizer is {prediction[0]}"
    return render_template('page2.html', prediction_text=output)

if __name__ == '__main__':
    app.run(debug=True)  # Consider switching off debug mode in production
