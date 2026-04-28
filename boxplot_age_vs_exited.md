# Understanding the 'Age vs Exited' Boxplot (ELI10 Style)

This plot helps us compare the ages of customers who **stayed** versus those who **left** the bank. It’s a visual summary of how age relates to churn.

---

### 🧩 What You’re Seeing

- **X-axis (bottom):** two groups — `0` (customers who stayed) and `1` (customers who left).
- **Y-axis (side):** customer **Age**.
- Each box shows how ages are spread within that group.

---

### 📦 How to Read a Boxplot

1. **The thick box:** shows where the middle 50% of the data lives (the most common ages).  
   The **line inside the box** is the **median** — the “typical” age.

2. **The thin lines (whiskers):** show the range of the rest of the data (younger to older customers).

3. **The small circles:** are **outliers** — customers who are unusually young or old compared to everyone else.

---

### 📊 What This Plot Tells You

- **Exited = 0 (stayed):**
  - Most customers are in their **mid-30s**.
  - There’s a wider base at younger ages, meaning more young people stayed.

- **Exited = 1 (left):**
  - The median is higher — around **40–50 years old**.
  - The whole box is shifted upward, meaning **older customers are more likely to leave**.
  - A few small circles below show very young customers who left (outliers).

---

### 🧠 ELI10 Summary

It’s like this:
> Younger customers tend to stay, while older customers are more likely to leave.

So, **Age** is an important feature — it clearly influences whether a customer stays or churns.

