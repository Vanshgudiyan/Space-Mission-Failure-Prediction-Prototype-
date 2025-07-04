# Step 1: Import the libraries
# pandas for data handling, matplotlib for plotting, sklearn for ML
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Step 2: Load the CSV data
# This file contains readings from a space mission over time
data = pd.read_csv('data/space_data.csv')

# Step 3: Print the first few rows to understand the data format
print("Sample data:")
print(data.head())

# Step 4: Check if any values are missing
# It's important to make sure there's no empty data
print("\nMissing values in columns:")
print(data.isnull().sum())

# Step 5: Drop rows with any missing values (for simplicity)
data = data.dropna()

# Step 6: Select input features and the target (failure)
# Features we'll use to predict: temperature, vibration, voltage
# Target column: failure (1 = failure occurred, 0 = no failure)
X = data[['temperature', 'vibration', 'voltage']]
y = data['failure']

# Step 7: Split the data into training and test sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 8: Train the model
# We'll use Random Forest because it's good for classification and easy to understand
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 9: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 10: Evaluate the model
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 11: Optional visualization — show how temperature affects failure
plt.figure(figsize=(8, 5))
plt.scatter(data['temperature'], data['failure'], alpha=0.6, color='red')
plt.title("Temperature vs Failure")
plt.xlabel("Temperature")
plt.ylabel("Failure (1 = Yes, 0 = No)")
plt.grid(True)
plt.tight_layout()
plt.show()
