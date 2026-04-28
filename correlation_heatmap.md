# Understanding the Correlation Heatmap (ELI10 Style)

This colorful chart shows how features in your dataset are related to each other. It helps us spot which variables move together and which ones go in opposite directions.

---

### 🧩 What It Shows

Each small square compares two features and gives a number between **-1** and **+1**:
- **+1** → They rise and fall together (strong positive relationship)
- **-1** → When one goes up, the other goes down (strong negative relationship)
- **0** → No real connection

The color helps you see this fast:
- **Red** = strong positive connection
- **Blue** = strong negative connection
- **Light or pale colors** = weak or no connection

---

### 🧠 How to Read It

Focus on the **“Exited”** row — that’s our churn indicator (who left the bank). The numbers beside each feature show how much that feature relates to churn.

| Feature | Correlation with Exited | What It Means |
|----------|-------------------------|----------------|
| **Age (0.36)** | Positive | Older customers are more likely to leave. |
| **IsActiveMember (-0.14)** | Negative | Active members are less likely to leave. |
| **Balance (0.12)** | Slight positive | Higher balances link slightly to higher churn. |
| **Gender (-0.11)** | Slight negative | Males might churn a bit less than females. |
| **Geography_Germany (0.17)** | Positive | Customers in Germany leave more often. |
| **Geography_Spain (-0.054)** | Slight negative | Customers in Spain leave slightly less. |

Other features like **CreditScore**, **Tenure**, or **EstimatedSalary** have numbers close to zero — meaning they don’t seem to affect churn much.

---

### 🧩 Relationships Between Features

You can also look at how features relate to each other:
- **Balance vs Geography_Germany (0.4):** German customers tend to have higher balances.
- **NumOfProducts vs Balance (-0.3):** People with more products often keep lower balances.

These insights help us understand which features overlap or might explain each other.

---

### 🎯 ELI10 Summary

Think of this heatmap as a **friendship map** for your data:
- **Red squares** → good friends (they move together)
- **Blue squares** → opposites (they move in opposite directions)
- **Light squares** → strangers (no clear link)

From this heatmap, we learn:
> Older, less active, or German customers are slightly more likely to leave the bank.

This helps us focus on features that actually matter for predicting churn.