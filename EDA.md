# Step 2: Exploratory Data Analysis (ELI10 Style)

Now that our data is clean and ready, let’s explore it! This part helps us understand what’s going on before we start training our model. Think of it like looking at a map before planning your route.

---

## 1. Import Tools for Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns
```
**Explanation:**
- `matplotlib` and `seaborn` help us make charts and graphs.
- Visuals make it easier to see trends and patterns in our data.

---

## 2. Basic Data Overview
```python
print(df.shape)      # Rows and columns
print(df.info())     # Data types and non-missing counts
print(df.describe()) # Quick stats like mean, min, max
```
**Explanation:**
- `df.shape` tells us how big the dataset is (rows × columns).
- `df.info()` shows which columns are numbers or text, and if any data is missing.
- `df.describe()` gives basic stats (like average and range) for numeric columns.

This helps us quickly spot weird values or columns that might not be useful.

---

## 3. Check Churn Distribution
```python
sns.countplot(x='Exited', data=df)
plt.title('Churn Distribution')
plt.show()
```
**Explanation:**
This shows how many customers left (`Exited=1`) vs. stayed (`Exited=0`). If one group is much smaller, it means our data is **imbalanced** — we’ll handle that later during modeling.

---

## 4. Explore Numeric Features
```python
numeric_cols = ['CreditScore','Age','Tenure','Balance','NumOfProducts','EstimatedSalary']
df[numeric_cols].hist(bins=20, figsize=(10,6))
plt.suptitle('Numeric Feature Distributions')
plt.show()
```
**Explanation:**
Histograms show how values are spread. For example:
- A spike at low `CreditScore` could mean many customers with poor credit.
- `Age` might show which age group dominates your customer base.

This helps spot skewed or unusual distributions.

---

## 5. Correlation Heatmap
```python
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
```
**Explanation:**
This chart shows how features move together:
- Positive (closer to 1): both go up together.
- Negative (closer to -1): one goes up, the other goes down.
- Near zero: no strong link.

It’s a great way to find redundant or highly related columns — we might remove some later if they overlap too much.

---

## 6. Relationships with Churn
```python
sns.boxplot(x='Exited', y='Age', data=df)
plt.title('Customer Age vs. Churn')
plt.show()

sns.boxplot(x='Exited', y='Balance', data=df)
plt.title('Balance vs. Churn')
plt.show()

sns.boxplot(x='Exited', y='CreditScore', data=df)
plt.title('Credit Score vs. Churn')
plt.show()
```
**Explanation:**
Boxplots show how numeric values differ between churned and retained customers. For example:
- If churned customers have higher balances, it may mean wealthier customers are leaving.
- If older customers churn more, the bank may need better retention offers for that group.

---

## 7. Categorical Feature Analysis
```python
categorical_cols = ['Gender','Geography_Germany','Geography_Spain']
for col in categorical_cols:
    sns.barplot(x=col, y='Exited', data=df)
    plt.title(f'{col} vs. Churn Rate')
    plt.show()
```
**Explanation:**
This compares churn rates between different groups:
- Do men or women churn more?
- Which country shows the highest churn?

Such insights help the business side design better retention strategies.

---

## 8. Quick Insights Summary
After EDA, we might find patterns like:
- Customers from one region churn more.
- Low activity (`IsActiveMember=0`) links to higher churn.
- Age and CreditScore have a moderate relationship with churn.

---

## 9. Next Step
Now we understand our data! The next phase will be **Feature Engineering and Modeling**, where we’ll build predictive models and make them explainable using SH