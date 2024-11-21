# Email Spam Classification Application

An interactive web-based application built using **Streamlit** to classify email messages as **Spam** or **Not Spam** using a trained machine learning model. This project demonstrates the power of **Natural Language Processing (NLP)** combined with **Machine Learning** to solve real-world problems.

---

## Features

- **Input Email Text**: Classify email messages by simply entering the content.
- **Real-Time Prediction**: Get instant feedback on whether the email is spam or not.
- **Intuitive Interface**: Built with Streamlit for a simple and responsive user experience.
- **Machine Learning Model**: Powered by a **Random Forest Classifier** trained on text data transformed by a `CountVectorizer`.

---

## How It Works

1. Input an email message into the text box provided.
2. The application processes the input and transforms it using a pre-trained `CountVectorizer`.
3. A trained **Random Forest Classifier** predicts the label:
   - `Ham`: Not Spam
   - `Spam`: Unsolicited or unwanted email
4. Results are displayed on the screen with clear visual feedback.

https://spam-email-classification-by-ashwith.streamlit.app/

---

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: For building the web application
- **Scikit-learn**: Machine learning library used for text vectorization and model training
- **Pandas & NumPy**: Data manipulation and numerical operations
- **Pickle**: For saving and loading the model and vectorizer

---

## Author

Developed by Madishetti Ashwith Kumar (https://github.com/mm8886).
