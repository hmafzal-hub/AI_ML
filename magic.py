import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

cols = ["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]
df = pd.read_csv(r"magic+gamma+telescope\magic04.data", names= cols)
df.head()

df['class'].unique()

df['class'] = (df['class'] == 'g').astype(int)

df.head()

for lbl in cols[:-1]:
  plt.hist(df[df['class'] == 1][lbl], color='blue', label='gamma', alpha= 0.7, density=True)
  plt.hist(df[df['class'] == 0][lbl], color='red', label='hadron', alpha= 0.7, density=True)
  plt.title(lbl)
  plt.ylabel('Probability')
  plt.xlabel(lbl)
  plt.legend()
  plt.show()

# train, validate, test = np.split(df.sample(frac=1),[int(0.6*len(df)),int(0.8 * len(df))])

# Shuffle dataframe
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Train/validate/test splits
train = df_shuffled.iloc[:int(0.6*len(df_shuffled))]
validate = df_shuffled.iloc[int(0.6*len(df_shuffled)):int(0.8*len(df_shuffled))]
test = df_shuffled.iloc[int(0.8*len(df_shuffled)):]


# def scale_data(dataframe, oversample = False):
#   X = dataframe[dataframe.columns[:-1]].values
#   y = dataframe[dataframe.columns[-1]].values

#   scaler = StandardScaler()

#   X = scaler.fit_transform(X)

#   if oversample:
#     ros = RandomOverSampler()
#     X, y = ros.fit_resample(X, y)

#   data = np.hstack((X, np.reshape(y, (-1,1))))

#   return data, X, y

def scale_data(dataframe, oversample=False):
    X = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    if oversample:
        ros = RandomOverSampler()
        X, y = ros.fit_resample(X, y)

    # Rebuild DataFrame with same feature names + target column
    feature_cols = dataframe.columns[:-1]
    target_col = dataframe.columns[-1]
    data = pd.DataFrame(np.hstack((X, np.reshape(y, (-1, 1)))),
                        columns=list(feature_cols) + [target_col])

    return data, X, y


print(len(train[train['class'] == 1])) # gamma
print(len(train[train['class'] == 0]))

train, X_train, y_train = scale_data(train, oversample=True)

len(y_train)

sum(y_train == 1)

sum(y_train == 0)

train, X_train, y_train = scale_data(train, oversample=True)
validate, X_valid, y_valid = scale_data(train, oversample=False)
test, X_test, y_test = scale_data(train, oversample=False)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train,y_train)

y_pred = knn_model.predict(X_test)

y_pred

y_test

print(classification_report(y_test,y_pred))



