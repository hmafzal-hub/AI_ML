# Step 4: Modeling (ELI10 Style)

Now that we’ve cleaned, explored, and engineered our data, it’s time to train our **machine learning models** to predict churn. Think of this step as teaching the computer how to recognize which customers are likely to leave.

---

## 🧩 1. Split the Data
We already split our data earlier:
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y)
```
**Explanation:**
- 80% of the data is for **training** (teaching the model).
- 20% is for **testing** (checking how well it learned).
- `stratify=y` ensures both sets have the same proportion of churners.

---

## 🧠 2. Choose Models to Try
We’ll try several models and compare them. Each one learns differently:

| Model | Description | Why Use It |
|--------|--------------|-------------|
| **Logistic Regression** | A simple yes/no predictor | Great for baseline comparison |
| **Random Forest** | A bunch of small decision trees voting together | High accuracy and interpretability |
| **XGBoost / LightGBM** | Advanced gradient boosting models | Often top performers for churn prediction |
| **KNN / SVM (optional)** | Find patterns in distances or boundaries | Good for exploration |

---

## ⚙️ 3. Train and Predict
Example using **Random Forest**:
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
```
**Explanation:**
- The model learns patterns during `.fit()`.
- It makes predictions on unseen data using `.predict()`.

---

## 📊 4. Evaluate the Model
We measure how well the model did using common metrics:
```python
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

**Metrics Explained (ELI10 Style):**
- **Accuracy:** How often the model is right overall.
- **Precision:** Of those predicted to churn, how many actually did.
- **Recall:** Of all real churners, how many the model caught. *(Important for churn!)*
- **F1-score:** The balance between precision and recall.
- **Confusion Matrix:** A 2x2 grid showing correct and incorrect predictions.

---

## 🧾 5. Compare Models
Train a few models and compare their scores:

| Model | Accuracy | Recall | AUC |
|--------|-----------|---------|------|
| Logistic Regression | 0.82 | 0.58 | 0.79 |
| Random Forest | 0.86 | 0.63 | 0.85 |
| XGBoost | 0.88 | 0.67 | 0.88 |

**Explanation:**
- **Accuracy** → overall success rate.
- **Recall** → how many churners we caught.
- **AUC (Area Under ROC Curve)** → higher = better model overall.

Choose the one that balances high recall and accuracy — often **XGBoost or Random Forest** wins.

---

## 🔍 6. Explain the Model (Optional but Useful)
Once you pick your best model, use tools like **SHAP** or **LIME** to explain predictions:
```python
import shap
explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values[1], X_test)
```
**Explanation:**
This shows which features push a customer toward churning or staying. It makes the model transparent and builds trust.

---

## ✅ ELI10 Summary
- We **train models** to spot patterns of customers likely to leave.
- We **test models** to check how well they predict unseen data.
- We **compare models** to pick the best one (usually XGBoost or Random Forest).
- We **explain predictions** so humans can understand what the model sees.

Next, we’ll move on to **Step 5: Model Explainability (SHAP/LIME)** — where we visually explain *why* the model predicts churn for each customer.