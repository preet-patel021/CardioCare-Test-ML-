# ❤️ CardioCare Test – Heart Disease Prediction System

### Your Heart. Your Health. Know Your Numbers.

CardioCare Test is a machine learning-based web application that predicts heart disease categories using health-related parameters. Built with Python and Streamlit, it provides an interactive dashboard where users can enter clinical measurements and receive a model-generated prediction.

## 🌟 Features

- ❤️ **Heart Disease Prediction:** Uses a trained Logistic Regression model.
- 👤 **Personal Information:** Accepts age and sex.
- 🩺 **Health Measurements:** Includes resting blood pressure, cholesterol, and fasting blood sugar.
- 📊 **Heart Performance Analysis:** Uses maximum heart rate, chest pain type, resting ECG, exercise-induced angina, oldpeak, and ST slope.
- 📈 **Prediction Probability:** Displays the model's positive-class probability when supported.
- 🎨 **Modern Dashboard:** Features a dark theme, interactive controls, and styled prediction results.
- ⚡ **Instant Results:** Processes submitted health measurements and displays the model's classification.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web application |
| Pandas | Input data preparation |
| Scikit-learn | Machine learning model and scaling |
| Joblib | Loading saved model artifacts |
| HTML and CSS | Dashboard styling |

## 🧠 Machine Learning Model

The application uses a trained **Logistic Regression** model to classify input data into the model's heart-disease-positive or heart-disease-negative category.

The prediction process includes:

1. Collecting health measurements from the user.
2. Converting categorical selections into model features.
3. Arranging input columns in the expected training order.
4. Scaling the input using the saved scaler.
5. Generating a prediction using the trained model.
6. Displaying the prediction and positive-class probability, when available.

## 📋 Input Parameters

The application accepts the following inputs:

- Age
- Sex
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Chest Pain Type
- Exercise-Induced Angina
- Oldpeak (ST Depression)
- ST Slope

## 📁 Project Structure

```text
CardioCare/
├── app.py
├── Logistic_Regression_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

*Keep the model files in the same directory as `app.py`, or update the file paths in your code accordingly.*

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR-GITHUB-REPOSITORY-URL
cd YOUR-REPOSITORY-FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install streamlit pandas scikit-learn joblib
```

### 4. Run the application

Navigate to the directory containing `app.py` and the model files, then execute:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 🎯 Project Objective

The main objective of CardioCare Test is to demonstrate how machine learning can be integrated into a simple, interactive healthcare application. It helps users explore how different health measurements are processed by a trained classification model.

## 🔮 Future Enhancements

- Add visual charts for health measurements.
- Improve model evaluation and explainability.
- Add downloadable prediction reports.
- Enhance mobile responsiveness.
- Add secure user profiles and assessment history.
- Deploy the application online for demonstration purposes.

## ⚠️ Medical Disclaimer

CardioCare Test is an educational machine learning project, not a medical diagnostic tool. Its predictions do not confirm or rule out heart disease. Consult a qualified healthcare professional for medical advice.

## 👨‍💻 Developer

**Preet Patel**  
Computer Science & Engineering  
Dayananda Sagar University (DSU), Bengaluru

## 📄 License

Choose and add an appropriate license file if you intend to distribute or share this project.

---

**CardioCare Test — Using Machine Learning to Make Heart Health Insights More Accessible. ❤️**
