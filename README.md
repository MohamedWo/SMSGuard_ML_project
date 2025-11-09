# 📩 SMS Spam Classifier

## 🧠 Overview
This project is a **Natural Language Processing (NLP)** model that classifies SMS messages as either **spam** or **ham** (not spam).  
It uses the **Multinomial Naive Bayes** algorithm and a **Bag-of-Words** model implemented with `CountVectorizer`.

---

## 📊 Dataset
**Dataset:** [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

- **Total samples:** 5572 messages  
- **Columns:**
  - `label` → message type (`ham` or `spam`)
  - `message` → text of the message

---

## ⚙️ Technologies Used
- Python 🐍  
- pandas  
- numpy  
- scikit-learn  
- seaborn  
- matplotlib  

---

## 🚀 Project Workflow
1. **Load dataset** and clean unnecessary columns  
2. **Text preprocessing**  
   - Remove special characters and symbols  
   - Convert to lowercase  
   - Remove stop words  
3. **Convert text to numerical vectors** using `CountVectorizer`  
4. **Split dataset** into training and testing sets  
5. **Train model** using `MultinomialNB`  
6. **Evaluate model** using:
   - Accuracy
   - Confusion Matrix
   - Classification Report  
7. **Predict new unseen messages**

---

## 📈 Model Performance
**Accuracy:** `97%`

**Classification Report:**
