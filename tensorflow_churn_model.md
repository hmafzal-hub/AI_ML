# Customer Churn Prediction with TensorFlow (ELI10 Style)

This guide explains how to build and train a **Neural Network using TensorFlow** to predict customer churn. We’ll go step by step — from scaling data to evaluating results — in a simple, easy-to-grasp way.

---

## 🧩 Step 1: Prepare and Scale Data
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler

# Scale the data (neural nets are sensitive to unscaled inputs)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**Why scaling matters:** Neural networks learn faster and more reliably when all inputs are on a similar scale — it helps the model focus on patterns instead of being confused by large numbers.

---

## 🧠 Step 2: Build the Neural Network Model
```python
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])
```

**ELI10 Explanation:**
- `Dense(64, relu)` → A layer of 64 mini-calculators (neurons) learning patterns.
- `Dropout(0.3)` → Turns off 30% of neurons randomly to avoid overfitting.
- Another `Dense(32, relu)` → Learns deeper, hidden relationships.
- Final `Dense(1, sigmoid)` → Outputs a probability between 0 and 1 — how likely a customer will churn.

---

## ⚙️ Step 3: Compile the Model
```python
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy', tf.keras.metrics.Recall(), tf.keras.metrics.AUC()]
)
```

**ELI10 Explanation:**
- **Adam** → A smart optimizer that adjusts learning automatically.
- **Binary Crossentropy** → Measures how far predictions are from the truth (churn = 1, stay = 0).
- **Metrics:** We track Accuracy, Recall (for churners), and AUC (overall prediction power).

---

## 🚀 Step 4: Train the Model
```python
history = model.fit(
    X_train_scaled, y_train,
    validation_data=(X_test_scaled, y_test),
    epochs=50,
    batch_size=32,
    verbose=1
)
```

**ELI10 Explanation:**
- **Epochs (50)** → How many times the model looks through the full dataset.
- **Batch size (32)** → Number of customers looked at before updating itself.
- **Validation data** → Helps check performance on unseen customers during training.

---

## 📊 Step 5: Evaluate the Model
```python
results = model.evaluate(X_test_scaled, y_test)
print(f"Test Accuracy: {results[1]:.2f}")
print(f"Test Recall: {results[2]:.2f}")
print(f"Test AUC: {results[3]:.2f}")
```

**Expected Results:**
| Metric | Expected Range |
|---------|----------------|
| **Accuracy** | 0.85 – 0.88 |
| **Recall (Churners)** | 0.60 – 0.70 |
| **AUC** | 0.85 – 0.90 |

**Interpretation:**  
If Recall ≥ 0.65 and AUC ≥ 0.85, your model is doing great — it’s catching churners well and separating them clearly from stayers.

---

## 📉 Step 6: Visualize Learning Progress
```python
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.plot(history.history['val_recall'], label='Validation Recall')
plt.plot(history.history['val_auc'], label='Validation AUC')
plt.legend()
plt.title('Training Progress')
plt.xlabel('Epochs')
plt.ylabel('Score')
plt.show()
```

**ELI10 Explanation:**  
This graph shows how the model learns over time — whether it’s improving steadily or overfitting (memorizing training data too much).

---

## ✅ ELI10 Summary
Think of your TensorFlow model as a **tiny brain**:
- It looks at customer examples again and again (epochs).
- It learns which combinations of features (age, balance, activity, etc.) signal churn.
- Dropout keeps it from memorizing.
- You track **Recall** and **AUC** to see how well it’s identifying likely leavers.

If done right, the TensorFlow model can match or even beat your Random Forest — especially after fine-tuning layers, learning rate, and dropout rates.