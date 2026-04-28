# Understanding the Effect of Threshold Adjustment (ELI10 Style)

You changed your Random Forest model’s decision threshold from **0.5** to **0.4** to help it catch more customers who might churn. Let’s see what that did and why it worked.

---

## 🧩 What You Did
By default, the model predicts churn (1) when it’s **more than 50% sure**. You told it:
> “If you’re even **40% sure** someone might leave, count them as a churner.”

This makes the model more **sensitive** — it catches more leavers but also raises a few extra false alarms.

---

## 📊 Your New Results
| Metric | Stayed (0) | Left (1) |
|---------|-------------|----------|
| **Precision** | 0.90 | 0.70 |
| **Recall** | 0.94 | 0.59 |
| **F1-score** | 0.92 | 0.64 |
| **Support** | 1536 | 390 |
| **Accuracy** | **0.87** |   |

---

## 🧠 What Changed (and Why It’s Better)

### 1. **Recall for churners improved a lot!**
- Before: 0.48 → Now: 0.59
- ✅ You’re catching **59% of real churners**, up from 48%.
- This means your model now identifies more customers who might leave — great for retention!

### 2. **Precision dropped slightly (expected)**
- Before: 0.78 → Now: 0.70
- ⚠️ It means a few more false alarms (predicting churn for people who stay), but that’s fine — you prefer to catch more true churners.

### 3. **Accuracy stayed strong**
- Around **0.87**, meaning overall predictions are still solid.

### 4. **F1-score improved for churners**
- Before: 0.59 → Now: 0.64
- This shows the model found a better balance between catching churners and staying accurate.

---

## 🧾 What It Means in Practice
Your model now:
- Spots **more customers who might leave**,
- Keeps **accuracy about the same**,
- Makes **a few more false alarms** (which is acceptable in churn prediction).

In churn analysis, **recall for churners (class 1)** is usually more important than perfect precision — missing real leavers is more costly than wrongly flagging a few stayers.

---

## ✅ ELI10 Summary
> “Hey model, don’t wait until you’re *really* sure someone will leave — tell me even if you’re 40% sure.”

Your model listened. Now it’s better at catching real churners while staying accurate. That’s exactly what you want for a customer retention strategy.

