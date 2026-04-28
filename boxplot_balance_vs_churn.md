# Understanding the 'Balance vs Churn' Boxplot (ELI10 Style)

This chart shows how customer **balances** differ between those who **stayed** and those who **left** the bank. It helps us see if the amount of money in an account affects the chance of churn.

---

### 🧩 What the Chart Shows

- **`Exited = 0`** → Customers who **stayed**.
- **`Exited = 1`** → Customers who **left (churned)**.
- **Y-axis:** Balance — how much money customers have in their accounts.

Each box represents how balances are spread within each group.

---

### 📊 What We Can See

1. **Stayed Customers (`Exited = 0`):**
   - Most balances are between **0 and ~130,000**.
   - The median (middle line in the box) is around **90,000**.
   - The spread is wide — many people with small balances, and some with very large ones.

2. **Churned Customers (`Exited = 1`):**
   - The median is a bit **higher**, around **110,000**.
   - Their balances stretch further upward — some have up to **250,000**.
   - The range is wider, showing both low and high balances among leavers.

---

### 🧠 What This Means

You’re right — churned customers tend to have **slightly higher balances**.  
This could mean:
- People with more money may expect better service or benefits.  
- High-balance customers might leave for better offers at other banks.  
- Customers with zero balances might be inactive but not officially closed out yet.

---

### ✅ ELI10 Summary

- Most customers who **stay** have balances below **130k**.
- Customers who **leave** often have **higher balances (80k–130k and above)**.
- Balance seems to play a small role — higher-balance customers are a bit more likely to churn.