# Data Preprocessing (ELI10 Style)

Let's make data ready for our customer churn prediction model. Think of it like cleaning and organizing ingredients before cooking.

---

## 1. Import the Tools
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
```
**Explanation:**
- `pandas` and `numpy` help us handle data like spreadsheets.
- `train_test_split` divides our data into training and testing parts.
- `StandardScaler` makes numbers comparable (like putting everything on the same scale).
- `LabelEncoder` turns words (like 'Male' and 'Female') into numbers, since computers understand numbers better.

---

## 2. Load the Data
```python
df = pd.read_csv("Churn_Modelling.csv")   # Load dataset
df.head()
```
**Explanation:**
We’re loading the file named `Churn_Modelling.csv` and showing the first few rows to get a quick look.

---

## 3. Drop Useless Columns
```python
df.drop(['RowNumber','CustomerId','Surname'], axis=1, inplace=True)
```
**Explanation:**
These columns are just IDs — they don’t help predict churn. We remove them to avoid noise.

---

## 4. Handle Missing Values and Outliers
```python
# Check for missing values
print(df.isnull().sum())

# Fill empty numeric spots with the column's middle value
df.fillna(df.median(numeric_only=True), inplace=True)

# Remove extreme outliers for certain columns
for col in ['CreditScore','Age','Balance','EstimatedSalary']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]
```
**Explanation:**
- First, we check if any data is missing.
- Then, we fill missing numeric values with the **median** (the middle number).
- Next, we remove **outliers** — extreme values that might confuse our model. We use something called the **Interquartile Range (IQR)**, which is like trimming the weird edges off a dataset.

---

## 5. Turn Words into Numbers
```python
# Gender: convert Male/Female to 0/1
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Geography: create separate columns for each country
df = pd.get_dummies(df, columns=['Geography'], drop_first=True)
```
**Explanation:**
- For `Gender`, we use `LabelEncoder` to change text into numbers (e.g., Male → 1, Female → 0).
- For `Geography`, we use **one-hot encoding** — it makes one column per country (like `Geography_France`, `Geography_Germany`, etc.). The model will learn from these numeric flags.

---

## 6. Separate Features and Target
```python
X = df.drop('Exited', axis=1)  # Features (inputs)
y = df['Exited']                # Target (output)
```
**Explanation:**
Here we split the dataset into:
- `X`: everything that might affect churn (age, balance, salary, etc.)
- `y`: the thing we’re trying to predict (`Exited` means churned = 1 or stayed = 0)

---

## 7. Scale the Numbers
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
**Explanation:**
We use `StandardScaler` to make sure every feature is on a similar scale. Otherwise, big numbers (like salary) might overpower small ones (like tenure).

---

## 8. Split into Train and Test Sets
```python
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
```
**Explanation:**
- **80%** of the data goes into training, and **20%** into testing.
- `random_state=42` ensures we get the same random split every time (for reproducibility).
- `stratify=y` makes sure both training and testing sets have the same proportion of churned customers.

---

## 9. Check the Result
```python
print("Training set shape:", X_train.shape)
print("Test set shape:", X_test.shape)
print("Churn rate:", round(y.mean()*100, 2), "%")
```
**Explanation:**
This gives a quick overview of how many samples are in each set and how many customers churned overall. It’s a good sanity check before we start modeling.

---

Now the data is cleaned, encoded, scaled, and ready for exploration in **Step 2: EDA (Exploratory Data Analysis)**.