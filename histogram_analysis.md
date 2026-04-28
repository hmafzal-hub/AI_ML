# Understanding the Histogram Grid (ELI10 Style)

This histogram grid gives us a quick “story” about your numeric data — like taking a peek inside your dataset to see what kind of customers the bank has. Let’s break it down simply.

---

### 1. **CreditScore**

Looks like a **bell shape**, which means most customers have average credit scores (around 600–700), with fewer at the low and high ends.  
➡️ This tells us credit scores are nicely spread — no extreme imbalance here.

---

### 2. **Age**

You can see most customers are between **30 and 40 years old**.  
➡️ The bank has more middle-aged clients than younger or older ones.  
If churn depends on age, we’ll check if older or younger people tend to leave more.

---

### 3. **Tenure**

The bars are quite **even across 0 to 10 years**, meaning customers have a wide range of how long they’ve stayed.  
➡️ Tenure might not have a strong pattern yet, but we can check later if short-tenure customers churn more.

---

### 4. **Balance**

Notice a **big spike at zero** — lots of customers have no balance at all.  
➡️ Some customers might just keep an account open but don’t actively use it (a red flag for churn).  
Then you see a hump between 100k–150k, showing active customers with decent balances.

---

### 5. **NumOfProducts**

Only a few bars are high — mostly at **1 and 2 products**.  
➡️ Most customers use one or two bank products (like a checking account and maybe a credit card).  
Very few use 3 or 4, which could signal lower engagement overall.

---

### 6. **EstimatedSalary**

This one’s **pretty flat** — the salaries are spread out evenly.  
➡️ The bank serves customers across income levels, so salary alone might not explain churn.

---

### 🧠 Summary of What You’ve Learned

- Most customers are **middle-aged** with **average credit scores**.  
- **Many people have zero balances** — possible inactive users.  
- **Most customers use only 1–2 products.**  
- **Salaries vary evenly**, so income isn’t skewed.  
- The data looks clean and well distributed, so it’s ready for deeper analysis.

---

These insights help us understand the population before moving to the next step — finding which of these features most influence **customer churn**.