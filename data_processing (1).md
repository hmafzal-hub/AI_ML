# Step 2: Exploratory Data Analysis (ELI10 Style)

Now that our data is clean and ready, let’s explore it! This part helps us understand what’s going on before we start training our model. Think of it like looking at a map before planning your route.

---

## 1. Import Tools for Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns
```
**Explanation:**
These libraries let us create nice charts. Visuals help us *see* what’s happening in our data — patterns, trends, or oddities.

---

## 2. Basic Data Overview
```python
print(df.shape)      # Rows and columns
print(df.info())     # Data types and non-missing counts
print(df.describe()) # Quick stats like mean, min, max
```
**Explanation:**
This gives a quick snapshot:
- `df.shape`: how big the data is.
- `df.info()`: what type of data each column has.
- `df.describe()`: basic stats (like average and range) for numeric columns.

This helps us find if something looks strange — like weirdly large numbers or missing data.

---

## 3. Check Churn Distribution
```python
sns.countplot(x='Exited', data=df)
plt.title('Churn Distribution')
plt.show()
```
**Explanation:**
This shows how many people left (`Exited = 1`) versus stayed (`Exited = 0`). If one side is much smaller, our data is imbalanced — something to remember when training the model.

---

## 4. Numeric Feature Distributions
```python
numeric_cols = ['CreditScore','Age','Tenure','Balance','NumOfProducts','EstimatedSalary']
df[numeric_cols].hist(bins=20, figsize=(10,6))
plt.suptitle('Numeric Feature Distributions')
plt.show()
```
**Explanation:**
These histograms show how values spread across customers:
- **CreditScore:** most people are around 600–700.
- **Age:** most are in their 30s–40s.
- **Tenure:** spread evenly from 0–10 years.
- **Balance:** many have zero balance (inactive users!), others around 100k–150k.
- **NumOfProducts:** most use 1–2 products.
- **EstimatedSalary:** evenly spread, meaning all income levels are represented.

These give us a sense of our customer mix.

---

## 5. Correlation Heatmap
```python
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
```
**Explanation:**
This shows how features move together:
- Positive values → both go up together.
- Negative values → one goes up, the other goes down.
- Near zero → no strong connection.

It’s a quick way to find what might relate to churn or overlap with other columns.

---

## 6. Churn vs Numeric Features (Boxplots)
```python
sns.boxplot(x='Exited', y='Age', data=df)
plt.title('Age vs Churn')
plt.show()

sns.boxplot(x='Exited', y='Balance', data=df)
plt.title('Balance vs Churn')
plt.show()

sns.boxplot(x='Exited', y='CreditScore', data=df)
plt.title('Credit Score vs Churn')
plt.show()
```
**Explanation:**
Boxplots compare how features differ between people who stayed and people who left.
- Churners might have **lower credit scores** or **higher balances**.
- Younger customers might **stay longer**.

The bigger the difference between the two boxes, the more useful that feature is for predicting churn.

---

## 7. Churn vs Categorical Features (Barplots)
```python
sns.barplot(x='Gender', y='Exited', data=df)
plt.title('Gender vs Churn Rate')
plt.show()

sns.barplot(x='Geography_Germany', y='Exited', data=df)
plt.title('Germany vs Churn Rate')
plt.show()

sns.barplot(x='Geography_Spain', y='Exited', data=df)
plt.title('Spain vs Churn Rate')
plt.show()
```
**Explanation:**
Each bar shows the *average churn rate* for that group:
- One country might churn more than another.
- One gender may show slightly different churn rates.

This helps us spot which groups are at risk.

---

## 8. Pairwise Relationships (Optional)
```python
sns.pairplot(df[['CreditScore','Age','Balance','EstimatedSalary','Exited']], hue='Exited')
plt.show()
```
**Explanation:**
This shows how churned and non-churned customers cluster in relation to multiple features. Think of it as seeing where “leavers” and “stayers” hang out on the map.

---

## 9. Key Takeaways from EDA
- Many customers have **zero balances** → possibly inactive.
- **Age and Balance** seem related to churn.
- **Geography** might influence churn rate (Germany often higher in this dataset).
- **Most customers use 1–2 products** — maybe offering more services could help retention.

---

## 10. Next Step
Now that we know which features might matter, we’ll move to **Feature Engineering** and **Modeling** — building a churn prediction model and explaining its behavior with SHAP or LIME.

