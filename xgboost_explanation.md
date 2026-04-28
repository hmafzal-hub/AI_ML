# Understanding XGBoost with `scale_pos_weight` (ELI10 Style)

You trained an **XGBoost model** to predict churn, but your data is **imbalanced** — most customers stay (0), and only a few leave (1). Let’s understand what this code does and what your results mean.

---

## 🧩 What You Did
```python
from xgboost import XGBClassifier

xgb = XGBClassifier(scale_pos_weight=len(y_train[y_train==0]) / len(y_train[y_train==1]))
xgb.fit(X_train, y_train)
```

### 💡 Why This Matters
Your dataset has way more “stayers” than “leavers.” Without adjustment, the model would just predict everyone as **staying** to get high accuracy — but that’s useless for churn detection.

So we fix that using:
```python
scale_pos_weight = (number of stayers) / (number of leavers)
```
This tells XGBoost:
> “Churners are rare — pay more attention to them!”

Each churn example now counts more during training, balancing the model’s learning.

---

## ⚙️ Training the Model
```python
xgb.fit(X_train, y_train)
```
Now the model trains while treating churners as more important, helping it focus on patterns that predict who might leave.

---

## 📊 Evaluating the Model
```python
from sklearn.metrics import roc_auc_score, recall_score
print('Recall:', recall_score(y_test, y_pred))
print('AUC:', roc_auc_score(y_test, y_pred_prob))
```
Output:
```
Recall: 0.47
AUC: 0.85
```

### 🧠 What These Numbers Mean
| Metric | What It Tells You | Interpretation |
|---------|------------------|----------------|
| **Recall = 0.47** | How many real churners the model caught. | It found about **47% of leavers** — not perfect, but better than random guessing. |
| **AUC = 0.85** | How well the model separates churners from stayers overall. | **0.85 is strong!** The model can tell churners apart well. |

---

## 🎯 Why We Do This
Without `scale_pos_weight`, the model gets lazy — it predicts everyone will stay because that’s the majority class.  
Adding this weight tells it:
> “Don’t ignore churners just because they’re few — they’re the ones that matter most.”

This approach improves **recall (catching churners)** and usually boosts **AUC (overall accuracy for both classes)**.

---

## 💭 What to Expect Next
- After weighting, recall should **improve further** once you tune model parameters (`max_depth`, `learning_rate`, etc.) or adjust thresholds again.
- AUC above 0.8 means your model is **learning the right patterns** — you’re on the right track!

---

## ✅ ELI10 Summary
Imagine a teacher with a class of 100 students — 90 behave (stayers) and 10 cause trouble (churners). The teacher ignores the troublemakers because there are few of them.

You tell the teacher:
> “Each troublemaker counts as 9 students — pay closer attention!”

Now, the teacher notices their behavior better — just like XGBoost paying more attention to churners after using `scale_pos_weight`.

