from flask import Flask, request, render_template, jsonify, url_for
import pickle
import numpy as np

# --- Your Existing Setup ---
# (Make sure you have these lines or similar)

app = Flask(__name__)

# Load your trained models
# Use 'rb' (read binary) mode for pickle files
try:
    model = pickle.load(open('spam-sms-mnb-model.pkl', 'rb'))
    cv = pickle.load(open('cv-transform.pkl', 'rb'))
except Exception as e:
    print(f"Error loading models: {e}")
    model = None
    cv = None

# --- End of Existing Setup ---


@app.route('/')
def home():
    """Renders the main page."""
    return render_template('main.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handles the prediction request from the form."""
    if not model or not cv:
        return jsonify({'error': 'Models not loaded properly.'}), 500

    try:
        # 1. Get message from the form
        message = request.form['message']
        
        # 2. Transform the message
        data = [message]
        vect = cv.transform(data).toarray()
        
        # 3. Make prediction
        prediction = model.predict(vect)[0] # Get the 0 or 1

        # 4. Create the JSON response
        if prediction == 1:
            result_text = "This looks like Spam!"
            # Use 'SpamHound_Icon.png' for spam
            result_image = url_for('static', filename='SpamHound_Icon.png') 
        else:
            result_text = "This looks Safe."
            # Use 'Safe.png' for not-spam
            result_image = url_for('static', filename='Safe.png')

        # 5. Return JSON instead of rendering result.html
        return jsonify({
            'prediction_text': result_text,
            'prediction_image': result_image
        })

    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({'error': 'An error occurred during prediction.'}), 400


if __name__ == '__main__':
    app.run(debug=True)