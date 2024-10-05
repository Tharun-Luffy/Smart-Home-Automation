import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

file_path = "D:/Smart Home/Dataset/new.csv"
data = pd.read_csv(file_path)

X = data.iloc[:, :-1]
y = data['out']

# X['mean'] = X.mean(axis=1)
# X['std'] = X.std(axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) * 100
print(f'Test Accuracy: {accuracy}%')

test_row = [0.18,0.1,-1.07,-20.23,-3.42,-1.43,173.8,-169.21,-149.08,-25.23,-10.54,-142.63,-28.11,-10.54]
test_row_scaled = scaler.transform([test_row])
prediction = model.predict(test_row_scaled)

print(f'Predicted value for the 16th feature (out): {prediction[0]}')
