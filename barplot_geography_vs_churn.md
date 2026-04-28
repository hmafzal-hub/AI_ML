# Understanding the 'Geography vs Churn Rate' Bar Plots (ELI10 Style)

These bar plots show how **customer churn** differs by country — in this case, **Germany** and **Spain**.

---

### 🧩 What the Charts Show

- **Y-axis:** Churn rate — the fraction of customers who left (`Exited = 1`).
- **X-axis:** Whether a customer is from that country (`True`) or not (`False`).

So:
- `True` = customers **from that country**.
- `False` = customers **from all other countries**.

---

### 🇩🇪 Germany vs Churn Rate

- **Germany = True:** Churn rate ≈ **32%**.
- **Germany = False:** Churn rate ≈ **16%**.

➡️ Roughly **1 in 3 German customers** left the bank, while only **1 in 6** non-Germans did.

✅ This means **German customers are much more likely to churn**.  
It might be due to different expectations, service issues, or stronger competition in that region.

---

### 🇪🇸 Spain vs Churn Rate

- **Spain = True:** Churn rate ≈ **17%**.
- **Spain = False:** Churn rate ≈ **21%**.

➡️ Spanish customers are **less likely to churn** — they seem more stable and loyal compared to other regions.

✅ So, **Spain’s customers tend to stay**, showing higher satisfaction or engagement.

---

### 🧠 What This Means

- **Country clearly affects churn.**
- **Germany = high churn region** — something worth investigating.
- **Spain = low churn region** — possibly stronger customer satisfaction.

The bank might want to explore regional differences in services, pricing, or customer support.

---

### ✅ ELI10 Summary

- **German customers:** More likely to **leave (~32%)**.
- **Spanish customers:** More likely to **stay (~17%)**.
- Geography plays a **big role** in customer churn — where someone lives really does matter!