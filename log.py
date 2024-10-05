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

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred) * 100
print(f'Test Accuracy: {accuracy}%')

test_row = pd.DataFrame([[0.64,0.69,-0.3,1.82,-2.39,-0.04,63.65,-59.09,-1.56,65.7,32.91,59.73,-61.9,32.91]], 
                        columns=X.columns)

# test_row = pd.DataFrame([[0.42,-0.92,-0.07,-1.17,28.25,-0.84,-69.05,-26.27,-172.94,162.31,82.02,-136.84,53.36,82.02]], 
#                         columns=X.columns)

test_row_scaled = scaler.transform(test_row)
prediction = model.predict(test_row_scaled)

if (prediction[0]):
    print("Lights On")
else:
    print('Lights Off')

import joblib

joblib.dump(scaler,'scaler.pkl')

# Assuming 'model' is your trained model
joblib.dump(model, 'logistic_model.pkl')  # Save the model as a .pkl file

#print(f'Predicted value for the 16th feature (out): {prediction[0]}')
