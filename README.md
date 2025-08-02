
# ❤️ Heart Disease Detection App

This project is a machine learning-based web application that predicts the risk of heart disease based on user-provided medical inputs. It is built with **Python**, **Scikit-learn**, and **Streamlit**.

---

## 📊 Problem Statement

Heart disease is one of the leading causes of death globally. Early detection can significantly improve patient outcomes. This project uses a machine learning model to predict whether a patient is at risk of heart disease based on clinical data.

---

## 🛠️ Tech Stack

- Python 3
- Scikit-learn
- Pandas, NumPy
- Matplotlib, Seaborn
- Streamlit
- imbalanced-learn (SMOTE)
- Joblib
- Git, GitHub

---

## 📁 Project Structure

```
heart_disease_Detection/
├── app.py                            # Streamlit frontend
├── random_forest_heart_disease_model.pkl  # Trained ML model
├── heart.csv                         # Original dataset
├── heart_disease_detection.ipynb     # Final Jupyter notebook
├── requirements.txt                  # Python dependencies
├── config.toml                       # Streamlit theme config
└── README.md                         # Project overview (this file)
```

---

## 📌 Features

✅ Cleaned and preprocessed dataset  
✅ Handled outliers (e.g., capping cholesterol values)  
✅ Performed SMOTE to fix class imbalance  
✅ Trained and evaluated multiple models:  
   - Logistic Regression  
   - Random Forest (Best Model)  
   - Decision Tree  
   - Naive Bayes  
   - SVM  
✅ Cross-validation & ROC Curve  
✅ Saved model using Joblib  
✅ Built Streamlit web interface  
✅ Custom dark theme and hospital logo  
✅ GitHub-hosted, ready for deployment  

---

## 🔍 Dataset Info

Dataset: [Heart Disease UCI Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)  
Rows: 918  
Target variable: `HeartDisease` (1 = Yes, 0 = No)

---

## 📈 Model Evaluation

The **Random Forest Classifier** achieved the highest accuracy:

- ✅ Accuracy: 89.67%
- ✅ Precision: 90%
- ✅ Recall: 92%
- ✅ F1 Score: 91%
- ✅ Cross-validation accuracy: 86.67%

---

## 🚀 How to Run the App Locally

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/heart_disease_Detection.git
cd heart_disease_Detection
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 🖼️ Sample Screenshot

![App Screenshot](link_to_screenshot_if_available.png)

---

## 🌐 Live App (Optional)

If deployed via [Streamlit Cloud](https://streamlit.io/cloud), include your link here:

👉 [Live Demo](https://your-username.streamlit.app/)

---

## 📚 Final Jupyter Notebook

The complete notebook `heart_disease_detection.ipynb` contains:

- Data loading and cleaning  
- Outlier handling  
- SMOTE oversampling  
- Model comparison  
- ROC curve  
- Cross-validation  
- Model saving  

---

## 📦 Requirements

All required libraries are listed in `requirements.txt`.

---

## 🙌 Acknowledgments

- UCI & Kaggle for the dataset
- Streamlit for UI framework
- Scikit-learn & community

---

## 🧠 Author

**Afzal Shah** — CS Student & ML Intern @ UET Lahore

---
