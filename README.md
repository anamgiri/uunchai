# Plant Disease Prediction System

## Overview
The Plant Disease Prediction System is a machine learning model designed to identify and classify plant diseases based on images of plant leaves. This project was developed as part of the UUNCHAI program, aiming to assist farmers and gardeners in diagnosing plant health issues efficiently.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Image Classification**: Identify various plant diseases from leaf images.
- **User-Friendly Interface**: Simple and intuitive interface for easy usage.
- **Real-Time Predictions**: Quick predictions on uploaded images.
- **Data Visualization**: Visual representations of the model's performance.

## Technologies Used
- Python
- TensorFlow/Keras (for building the machine learning model)
- OpenCV (for image processing)
- Flask (for creating the web interface)
- HTML/CSS/JavaScript (for frontend development)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plant-disease-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd plant-disease-prediction
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000`.
3. Upload an image of a plant leaf to receive a prediction of the disease.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add your feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
