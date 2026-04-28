# Understanding the Pair Plot (ELI10 Style)

This plot — also called a **pair plot** or **scatterplot matrix** — helps us see how multiple numeric features relate to each other and to churn.

---

### 🧩 What the Plot Shows

- Each small square compares **two features** (like Age vs Balance).  
- **Blue dots (0)** = customers who **stayed**.  
- **Orange dots (1)** = customers who **left**.  
- The **diagonal plots** show how one feature is distributed on its own (like a mini histogram).

This lets us see patterns between different combinations of features.

---

### 🔍 How to Read It

#### 1. **CreditScore vs Others**
The blue and orange dots are all mixed together.  
➡️ That means **credit score doesn’t separate churners from non-churners** — people with good or bad scores leave about equally.

#### 2. **Age vs Others**
There are more **orange dots among older customers**.  
➡️ **Older people are more likely to leave.** Younger customers mostly stay.

#### 3. **Balance vs Others**
You can see churners (orange) clustering more around **medium to high balances**.  
➡️ People with **higher balances** might be more likely to leave.

#### 4. **EstimatedSalary vs Others**
Dots look evenly mixed across salaries.  
➡️ **Salary doesn’t have much impact** on churn.

---

### 🧠 Big Picture

- **Age** shows a clear pattern — older customers churn more.  
- **Balance** has a small effect — higher balances link to more churn.  
- **CreditScore** and **EstimatedSalary** don’t show much difference between churned and non-churned groups.

This confirms that some features (like Age and Balance) are more useful for predicting churn than others.

---

### ✅ ELI10 Summary

Think of this as a big **relationship map**:
- Each dot is a customer.  
- **Blue dots** stayed; **orange dots** left.  
- Where orange dots bunch up, that’s where churn risk is higher.

From this chart:
> Older age and higher balances are red flags for churn, while credit score and salary don’t matter much.
