# Model Comparison: Predicting Customer Churn (ELI10 Style)

You’ve now trained and tested **multiple models** — Logistic Regression, Random Forest, XGBoost, and Neural Network (MLP). Let’s compare them in plain English and see which one works best.

---

## 🧩 1. Logistic Regression
```python
AUC: 0.7877
```
| Metric | Stayed (0) | Left (1) |
|---------|-------------|----------|
| **Precision** | 0.91 | 0.40 |
| **Recall** | 0.73 | 0.72 |
| **F1-score** | 0.81 | 0.52 |
| **Accuracy** | 0.73 |

**Explanation:**  
- It’s a simple model that looks for linear relationships.  
- It catches **72% of churners** (recall) but isn’t great at precision — it rings a few false alarms.  
- AUC of **0.78** means it’s decent at separating churners from stayers.

✅ **Strength:** Good recall for churners, easy to interpret.  
⚠️ **Weakness:** Simplicity limits its accuracy.

---

## 🌲 2. Random Forest (previous result)
| Metric | Stayed (0) | Left (1) |
|---------|-------------|----------|
| **Precision** | 0.90 | 0.70 |
| **Recall** | 0.94 | 0.59 |
| **F1-score** | 0.92 | 0.64 |
| **Accuracy** | 0.87 |
| **AUC** | ~0.85 |

**Explanation:**  
- This model combines many decision trees that vote on each prediction.  
- It’s strong, balanced, and learns nonlinear relationships.  
- It performs better overall than Logistic Regression, with good accuracy and recall.

✅ **Strength:** Balanced performance, interpretable, stable.  
⚠️ **Weakness:** Slightly less recall than ideal for churn.

---

## ⚡ 3. XGBoost
```python
Recall: 0.47
AUC: 0.85
```
**Explanation:**  
- XGBoost is an upgraded version of tree models, very efficient and smart.  
- AUC of **0.85** means it’s good at distinguishing churners vs stayers, but recall is low — it misses over half the churners.

✅ **Strength:** High overall accuracy and efficiency.  
⚠️ **Weakness:** Recall (0.47) too low — needs threshold tuning or parameter adjustment.

---

## 🧠 4. Neural Network (MLP)
```python
AUC: 0.8261
```
| Metric | Stayed (0) | Left (1) |
|---------|-------------|----------|
| **Precision** | 0.88 | 0.64 |
| **Recall** | 0.93 | 0.52 |
| **F1-score** | 0.90 | 0.57 |
| **Accuracy** | 0.84 |

**Explanation:**  
- The Neural Network learns complex patterns using layers of neurons.  
- It performs close to Random Forest in accuracy and AUC but still struggles a bit with recall for churners.

✅ **Strength:** Learns hidden patterns and nonlinear relations.  
⚠️ **Weakness:** Harder to interpret, recall not much higher.

---

## 📊 Overall Comparison
| Model | Accuracy | Recall (Churners) | AUC | Notes |
|--------|-----------|------------------|------|-------|
| Logistic Regression | 0.73 | **0.72** | 0.78 | Best recall but lower overall accuracy |
| Random Forest | **0.87** | 0.59 | **0.85** | Strong all-rounder |
| XGBoost | 0.86 | 0.47 | **0.85** | High AUC, recall needs tuning |
| Neural Network | 0.84 | 0.52 | 0.83 | Good learner, similar to Random Forest |

---

## 🧭 What This Means
- **If you care most about catching churners:** Logistic Regression (high recall) or Random Forest (good balance).  
- **If you care most about overall accuracy and stability:** Random Forest or XGBoost.  
- **If you want a modern, flexible model:** Neural Network can be tuned for future improvement.

---

## ✅ ELI10 Summary
Imagine you’re trying to find which model is best at spotting customers about to leave:
- **Logistic Regression** → Like a simple calculator: fast and direct.
- **Random Forest** → Like a team of experienced advisors voting on each customer.
- **XGBoost** → Like a super-efficient advisor who learns from past mistakes.
- **Neural Network** → Like a mini brain that understands patterns no one else sees.

🎯 For your banking churn project, **Random Forest** gives the best overall balance between **accuracy** and **recall**, while **Logistic Regression** is a great backup when you prioritize **catching as many churners as possible**.