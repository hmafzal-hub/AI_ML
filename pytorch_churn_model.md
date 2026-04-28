# Customer Churn Prediction with PyTorch (ELI10 Style)

This guide explains how to build, train, and evaluate a **Neural Network using PyTorch** for customer churn prediction. Each step is written in an ELI10 style — so you can understand what’s happening and why.

---

## 🧩 Step 1: Import Libraries & Prepare Data
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.preprocessing import StandardScaler

# Scale and convert data to tensors
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_torch = torch.tensor(X_train_scaled, dtype=torch.float32)
X_test_torch = torch.tensor(X_test_scaled, dtype=torch.float32)
y_train_torch = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
y_test_torch = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

# DataLoaders for batching
train_data = TensorDataset(X_train_torch, y_train_torch)
test_data = TensorDataset(X_test_torch, y_test_torch)

train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader = DataLoader(test_data, batch_size=32)
```

### 💡 ELI10 Explanation
- PyTorch needs data as **tensors** (supercharged arrays that support gradient math).
- **DataLoader** breaks the dataset into small pieces (batches) for efficient learning.
- **Scaling** ensures every input (like Age or Balance) contributes fairly to the model.

---

## 🧠 Step 2: Build the Neural Network
```python
class ChurnNet(nn.Module):
    def __init__(self):
        super(ChurnNet, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(X_train_torch.shape[1], 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)

model = ChurnNet()
```

### 🧠 ELI10 Explanation
- Think of `nn.Linear()` layers as **neurons** that connect inputs to outputs.
- **ReLU** helps the network focus only on meaningful signals (sets negatives to zero).
- **Dropout** randomly turns off neurons to prevent the model from memorizing training data.
- **Sigmoid** squashes the output into a value between 0 and 1 (churn probability).

---

## ⚙️ Step 3: Define Loss and Optimizer
```python
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 💡 ELI10 Explanation
- **Loss function** measures how wrong the model is on each prediction.
- **Adam optimizer** adjusts the model’s weights smartly to minimize that loss.

---

## 🚀 Step 4: Train the Model
```python
epochs = 50
for epoch in range(epochs):
    model.train()
    running_loss = 0.0

    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        y_pred = model(X_batch)
        loss = criterion(y_pred, y_batch)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    print(f'Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}')
```

### 🧠 ELI10 Explanation
- Each **epoch** = the model looks at the entire dataset once.
- It **guesses → checks loss → adjusts → repeats**.
- The goal is for the loss to **get smaller** each round — meaning it’s learning.

---

## 📊 Step 5: Evaluate the Model
```python
from sklearn.metrics import classification_report, roc_auc_score

model.eval()
with torch.no_grad():
    y_pred_prob = model(X_test_torch).numpy()
    y_pred = (y_pred_prob >= 0.5).astype(int)

print(classification_report(y_test, y_pred))
print('AUC:', roc_auc_score(y_test, y_pred_prob))
```

### Expected Results
| Metric | Expected Range |
|---------|----------------|
| Accuracy | 0.84 – 0.87 |
| Recall (Churners) | 0.60 – 0.70 |
| AUC | 0.85 – 0.89 |

✅ If **Recall ≥ 0.65** and **AUC ≥ 0.85**, your model is performing well.

---

## 🧾 Step 6: Tuning Tips
- **Learning rate:** Try `0.0005` if the loss fluctuates.
- **Epochs:** Increase to `100` for deeper learning.
- **Network size:** Experiment with `(128, 64, 32)` layers for more complex learning.

---

## ✅ ELI10 Summary
Your PyTorch churn model works like a custom-built **tiny brain**:
- It learns from batches of data, spotting patterns like high balance or inactivity.
- Each neuron connects patterns across features.
- Over time, it improves recall (how many churners it catches) and AUC (how well it separates churners vs stayers).

In the end, you’ll have a model that’s accurate, flexible, and fully customizable — perfect for understanding customer churn behavior!