PySpam-Guard: ML Spam Classifier Web App

       An intelligent spam filter web app built with Python. Uses a Scikit-learn (Naive Bayes) model deployed via Flask to classify SMS messages as ham or spam in real-time.
      
      This is an end-to-end machine learning project that takes a raw dataset of SMS messages (`spam.csv`), builds a classification model, and deploys it as a simple web application using Flask.
<img width="972" height="782" alt="spam" src="https://github.com/user-attachments/assets/88541503-6dc5-48f3-ae82-ddb4a05cb31c" />


 🚀 Features

        * Real-Time Classification: Instantly classifies any user-inputted message as "Spam" or "Ham" (Not Spam).
        * ML Model Backend: Powered by a Multinomial Naive Bayes (MNB) model trained on the SMS Spam Collection Dataset.
        * Text Preprocessing: Includes a complete text processing pipeline using `CountVectorizer` (or `TfidfVectorizer`) to convert raw text into features.
        * Web Interface: A clean and simple UI built with HTML/CSS and powered by a Flask backend.



 🛠️ Technologies Used
      
        * Backend: Python, Flask
        * Machine Learning: Scikit-learn, Pandas, NumPy
        * ML Model: Multinomial Naive Bayes (MNB)
        * Data Processing: `CountVectorizer` (or TF-IDF)
        * Frontend: HTML, CSS


 ⚙️ Project Workflow & Architecture

This project follows a standard machine learning workflow:

1.  Data Loading: The `spam.csv` dataset is loaded into a Pandas DataFrame.
2.  Text Preprocessing:
      * Text cleaning (removing punctuation, lowercasing).
      * Vectorization: Raw text messages are converted into numerical vectors using `CountVectorizer`.
3.  Model Training: A Multinomial Naive Bayes classifier is trained on the processed data.
4.  Model Serialization: The trained vectorizer (`cv-transform.pkl`) and the model (`spam-sms-mnb-model.pkl`) are saved as `.pkl` files.
5.  Flask App:
      * The `app.py` file loads the saved models.
      * It serves the `main.html` frontend.
      * When a user submits a message, the app preprocesses the text, predicts the class, and returns the result to the user.


 🏃 How to Run Locally

Follow these steps to get the project running on your local machine.

Prerequisites:
    
      * Python 3.x
      * pip (Python package installer)
      
      1. Clone the Repository:
      
            ```bash
            git clone https://github.com/YOUR_USERNAME/PySpam-Guard.git
            cd PySpam-Guard
            ```
      
      2. Create and Activate a Virtual Environment:
      
            * On Windows:
              ```bash
              python -m venv venv
              .\venv\Scripts\activate
              ```
            * On macOS/Linux:
              ```bash
              python3 -m venv venv
              source venv/bin/activate
              ```
      
      3. Install Dependencies:
      
          ```bash
          pip install -r requirements.txt
          ```
      
      4. Run the Flask App:
      
          ```bash
          python app.py
          ```
      
      5. Open in Browser:
          Navigate to `http://127.0.0.1:5000` in your web browser to see the app live\!

