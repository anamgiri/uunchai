from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('stored_model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('page.html')  # Ensure your template file is named 'index.html' or change the name accordingly

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict(final)
    output = f"The predicted crop is {prediction[0]}"
    return render_template('page.html', prediction_text=output)  # Adjust your template to display the prediction_text variable

if __name__ == '__main__':
    app.run(debug=True)