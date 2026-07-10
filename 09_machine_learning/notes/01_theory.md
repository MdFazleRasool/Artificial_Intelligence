# 🤖 Introduction to Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-AI-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-Programming-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge">
</p>

---

## 📚 What is Machine Learning?

> Machine Learning (ML) is a branch of Computer Science where computers learn from data, identify patterns, and make decisions or predictions without being explicitly programmed for every task.

---

## 🧠 Types of Machine Learning

| Type                      | Description                             |
| ------------------------- | --------------------------------------- |
| 🎯 Supervised Learning    | Learns from labeled data                |
| 🔍 Unsupervised Learning  | Finds hidden patterns in unlabeled data |
| 🎮 Reinforcement Learning | Learns through rewards and penalties    |

---

## 🎯 Supervised Learning

> Supervised Learning trains algorithms using **labeled datasets**, where each input has a known correct output. The model learns patterns and predicts outcomes for unseen data.

---

## 📈 Types of Supervised Learning Problems

### 1️⃣ Regression

Predicts a **continuous numerical value**.

#### Examples

* 🏠 House Price Prediction
* 📊 Stock Price Prediction
* 🌡️ Temperature Forecasting

---

### 2️⃣ Classification

Predicts a **category or class**.

#### Examples

* 📧 Spam Email Detection
* 💳 Fraud Detection
* 🏥 Disease Prediction

---

## 🏷️ Types of Classification Problems

### 🔵 Binary Classification

Predicts one of **two classes**.

**Examples:**

* Yes / No
* Spam / Not Spam
* Fraud / Not Fraud

---

### 🟢 Multiclass Classification

Predicts one of **multiple classes**.

**Examples:**

* 🐶 Animal Species Prediction
* ✍️ Handwritten Digit Recognition (0-9)

---

### 🟣 Multilabel Classification

A single output can belong to **multiple classes simultaneously**.

**Examples:**

* 🎬 Movie Genre Prediction
* 🖼️ Image Tagging

---

## ⚙️ Scikit-Learn

**Scikit-Learn** is an open-source Machine Learning library built on top of:

* 🔢 NumPy
* 📐 SciPy
* 📊 Matplotlib

### ✨ Features

✅ Easy to Learn
✅ Open Source
✅ Efficient ML Algorithms
✅ Data Preprocessing Tools
✅ Model Evaluation Tools

### 📖 Supports

* 🎯 Supervised Learning
* 🔍 Unsupervised Learning

---

## 🚀 Popular Scikit-Learn Algorithms

| Algorithm                      | Use Case                    |
| ------------------------------ | --------------------------- |
| 📈 Linear Regression           | Regression                  |
| 🎯 Logistic Regression         | Classification              |
| 👥 K-Nearest Neighbors (KNN)   | Regression & Classification |
| 🌳 Decision Trees              | Regression & Classification |
| 📧 Naive Bayes                 | Classification              |
| ⚡ Support Vector Machine (SVM) | Classification & Regression |

---

# 📈 Linear Regression  ->
  ### Best Fit Line:- 
  ![alt text](image/01_Best_Fit_Line.png)

  ### Gradient Descent :-
  ![alt text](image/02_Gradient_Descent01.png)
  ![alt text](image/03_Gradient_Descent02.png)


  ## 1. Feature Engineering - Encoding ->()
  ![alt text](image/04_FeatureEngineering.png)

  ### 1.1 - One Hot Encoding
  ### 1.2 - Interaction Features
  ### 1.3 - overfitting
  ![alt text](image/05_overfitting.png)

  ### 1.3 - underfitting
  ![alt text](image/06_underfitting.png)

  ### 1.4 - fix_overfitting_&_underfitting
  ![alt text](image/07_fix_over-underfitting.png)

  ### 1.5 - regularization
  ![alt text](image/08_regularization.png)
    #### 1.5.1 - Lasso_Regression
    ![alt text](image/09_lasso_regression.png)
    
  #### 1.5.2 - ridge_regression
  ![alt text](image/10_ridge_regression01.png)

  ![alt text](image/11_ridge_regression02.png)

  #### 1.5.3 LassoCV - in pllace of Lasso_Regression 
  #### 1.5.4 ElasticNet 
  ![alt text](image/12_ElasticNet.png)


  ### important concepts covered->
  ![alt text](image/13_important_concepts.png)


# 📈 Logistic_Regression  ->
  ### - Summary of linear_regression
  ![alt text](image/14_linear_regression02.png)
  ![alt text](image/15_Logistic_Regression01.png)
  #### 1.1 - Sigmoid Function

  #### 1.2 - Cost_Function of Logistic_Regression
  ![alt text](image/16_LR_Cost_Function.png)
  ![alt text](image/17_LR_Cost_Function02.png)

  # Standardization of data
  ![alt text](image/18_Standardization.png)

  ### 1.3 - Confusion Matrix
  ![alt text](image/19_Confusion_Matrix.png)

  #### 1.4 - Evaluation_matrix :- ( Accuracy, Precision, Recall, F1-Score )
  ![alt text](image/20_Evaluation_Matrix.png)
  ![alt text](image/21_Evaluation_Matrix02.png)

  ## Naive Bayes Classifier
  ![alt text](image/22_Naive_Bayes01.png)
  ![alt text](image/23_Naive_Bayes02.png)
  ### eg:-
  ![alt text](image/24_Naive_Bayes_Example.png)
  Types of Naive Bayes Classifier :-
  ![alt text](image/25_Naive_Bayes_Types.png)

## KNN - k Nearest Neighbors
  ### steps to implement KNN :-
   ![alt text](image/26_KNN_Steps.png)
   ![alt text](image/27_KNN_Example.png)
   ### - limitations of KNN
   ![alt text](image/28_KNN_Limitations.png)

   #### Valdation Techniques :- 
   ![alt text](image/29_Validation_Techniques01.png)

   ![alt text](image/30_Validation_Techniques02.png)

   #### - CrossValidation :- 
   ![alt text](image/31_CrossValidation.png)
   ##### eg:- Hyperparameter Tuning
   ##### - GridSearchCV
   ##### - pipeline
   ![alt text](image/32_Pipeline.png)

  




  # 🌳 Decision Trees      ->          Regression & Classification 
  ![alt text](image/33_Decision_Trees_01.png)
  ### Entropy & Information Gain :- 
   ![alt text](image/34_Entropy.png)
   ### Gini Impurity :-
   ![alt text](image/35_Gini_Impurity.png)
   ### - impurity based on Entropy & Gini Impurity
   ![alt text](image/36_Impurity_Comparison.png)
   ### - Information Gain based on Entropy & Gini Impurity
   ![alt text](image/37_Information_Gain.png)
   #### - Pruning in Decision Trees
   ![alt text](image/38_Pruning.png)
   #### - Rules for Pruning :- 
   ![alt text](image/39_Pruning_Rules.png)

