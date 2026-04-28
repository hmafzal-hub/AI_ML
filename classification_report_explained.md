# Understanding the Classification Report (ELI10 Style)

Your model tries to predict whether a customer will **stay (0)** or **leave (1)**. The classification report tells us how well it did for each group.

---

## 📊 The Output
```
           precision    recall  f1-score   support

           0       0.88      0.97      0.92      1536
           1       0.78      0.48      0.59       390

    accuracy                           0.87      1926
   macro avg       0.83      0.72      0.76      1926
weighted avg       0.86      0.87      0.85      1926

[[1484   52]
 [ 204  186]]
```

---

## 🧩 What Each Metric Means

| Term | Meaning |
|------|----------|
| **Precision** | Of all the people the model predicted would churn, how many actually did? |
| **Recall** | Of all the people who truly churned, how many did the model catch? |
| **F1-score** | A balance between precision and recall — good for judging overall accuracy on a class. |
| **Support** | The number of actual samples for each group (how many stayed or left). |

---

## 💬 Reading Your Results

| Metric | Stayed (0) | Left (1) |
|---------|-------------|----------|
| **Precision** | 0.88 | 0.78 |
| **Recall** | 0.97 | 0.48 |
| **F1-score** | 0.92 | 0.59 |
| **Support** | 1536 | 390 |

### ✳️ What It Means
- **Precision for churn (0.78):** When the model predicts someone will leave, it’s right 78% of the time.
- **Recall for churn (0.48):** It finds only 48% of the people who actually left — it misses about half.
- **F1-score for churn (0.59):** Overall performance for predicting churn is okay but can improve.
- **Support:** There are 1536 customers who stayed and 390 who left.

---

## 🧾 Confusion Matrix
```
[[1484   52]
 [ 204  186]]
```

| | Predicted Stay (0) | Predicted Leave (1) |
|--|--------------------|--------------------|
| **Actually Stayed (0)** | ✅ 1484 correct | ❌ 52 wrong |
| **Actually Left (1)** | ❌ 204 missed | ✅ 186 correct |

### 🔍 Interpretation
- The model is **great at spotting who stays (97%)**.
- It **misses many churners (52%)**, catching less than half of them.

---

## 📈 The Big Picture
- **Precision** = “When I say someone will leave, how often am I right?”
- **Recall** = “Of everyone who left, how many did I find?”
- **F1-score** = “Am I balancing those two things well?”
- **Support** = “How many examples did I have?”

### ✅ ELI10 Summary
Your model is **excellent at finding customers who stay**, but **not great at catching all the leavers**. To improve:
- You could adjust the decision threshold.
- Or use models like **XGBoost** or **balanced Random Forest** that handle imbalanced data better.

In short: **High recall = fewer missed churners.** That’s your goal for churn prediction!