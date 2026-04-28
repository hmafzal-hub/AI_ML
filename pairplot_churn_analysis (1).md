# Step 3: Feature Engineering (ELI10 Style)

Now that we’ve explored our data, it’s time to make it smarter! **Feature engineering** means creating or transforming data columns so our model can learn better patterns. Think of it like giving your model better clues before it tries to solve a puzzle.

---

## 1. Why Feature Engineering Matters
Machine learning models only see numbers. The better those numbers represent real-world behavior, the smarter the model becomes. 

For example:
- Instead of just knowing how long someone’s been a customer (**Tenure**), the model could also know **how much they spend per year**.
- Instead of just having an average balance, we can show **how that balance changes over time**.

---

## 2. Creating New Features
Here are some helpful ideas for churn prediction:

### **a. Tenure Groups**
Group customers based on how long they’ve stayed:
```python
def tenure_group(x):
    if x <= 3:
        return 'New'
    elif x <= 6:
        return 'Intermediate'
    else:
        return 'Loyal'

df['TenureGroup'] = df['Tenure'].apply(tenure_group)
```
**Why:** This helps the model spot patterns — new customers might churn more often than loyal ones.

---

### **b. Balance-to-Salary Ratio**
Compare how much customers have saved relative to their income:
```python
df['BalanceSalaryRatio'] = df['Balance'] / (df['EstimatedSalary'] + 1)
```
**Why:** A high ratio might mean a customer already keeps a lot of money in the bank — they might leave if unhappy.

---

### **c. Credit Score per Age**
Normalize credit score by age to spot credit reliability differences:
```python
df['CreditScorePerAge'] = df['CreditScore'] / df['Age']
```
**Why:** Someone young with a good score might be more loyal than an older person with the same score.

---

### **d. IsHighValueCustomer**
Mark customers with strong engagement or large balances:
```python
df['IsHighValueCustomer'] = np.where((df['Balance'] > 100000) & (df['NumOfProducts'] > 1), 1, 0)
```
**Why:** This captures your “VIP” group — often key for retention analysis.

---

## 3. Transforming Existing Features
Sometimes we need to adjust or simplify data:

### **a. Log Transform Skewed Data**
Balances or salaries can be highly skewed (a few people with huge values). You can apply a log transform:
```python
import numpy as np
df['LogBalance'] = np.log1p(df['Balance'])
```
**Why:** Makes the data more balanced, so big numbers don’t dominate the model.

### **b. Encoding New Categorical Columns**
After creating columns like `TenureGroup`, use one-hot encoding:
```python
df = pd.get_dummies(df, columns=['TenureGroup'], drop_first=True)
```
**Why:** Converts text categories (New, Intermediate, Loyal) into numbers for the model.

---

## 4. Feature Selection
Too many features can confuse the model. Keep the most useful ones:
- Use **correlation** and **feature importance plots** to see which ones matter most.
- Drop features with little or no effect on churn.

Example:
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance.sort_values(ascending=False).head(10)
```
**Why:** This shows which features help the model predict churn best.

---

## 5. Scaling and Final Check
After adding new features:
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop('Exited', axis=1))
```
Check again for missing values or outliers. The model performs best when features are clean and consistent.

---

## ✅ ELI10 Summary
- Feature engineering = **giving your model better clues**.
- Create helpful ratios and categories (like Balance-to-Salary or TenureGroup).
- Scale and encode data so the model understands it.
- Drop features that don’t help much.

Next step: we’ll move to **Step 4: Modeling**, where we train our machine learning model to predict churn!

