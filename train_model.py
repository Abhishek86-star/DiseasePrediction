
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("disease_diagnosis.csv")

# Select features and target
features = [
    "Age",
    "Heart_Rate_bpm",
    "Body_Temperature_C",
    "Oxygen_Saturation_%"
]

X = df[features]
y = df["Diagnosis"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
print("Test Accuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Save as a new file; keep original model safe
with open("dp_new.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nSUCCESS: New model saved as dp_new.pkl")
