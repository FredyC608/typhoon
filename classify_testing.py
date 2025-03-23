import numpy as np
import pandas as pd
import joblib
# Import validation measures
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

df = pd.read_csv("PythonWorks\PythonBasics\Datathon\\final_depression_dataset_1.csv")
df.dataframeName = 'final_depression_dataset_1.csv'
df.info()
# Clean Data
df = df.drop(columns=["City", "Name", "Working Professional or Student", "Profession"])

# Convert "Depression" column from "Yes" or "No" to 1 and 0
df['Depression'] = df['Depression'].map({'Yes': 1, 'No': 0})

# df.info()
df = pd.get_dummies(df)
# Check for NaN
df = df.fillna(df.mean())
# df.info()

# Split data (80 train, 20 test)
from sklearn.model_selection import train_test_split
x = df.drop(columns=["Depression"]) # every column but "Depression and id"
y = df["Depression"].astype(int).values
x_train, x_validate, y_train, y_validate = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)

# Check importance of features
importances = rfc.feature_importances_
feature_names = x.columns

# Sort the feature importances
sorted_importances = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)

# Print the importance of each feature
# print("Feature Importances:")
# for feature, importance in sorted_importances:
#     print(f"{feature}: {importance}")

# Filter features with importance >= 0.04
important_features = [feature for feature, importance in sorted_importances if importance >= 0.04]


# Create a new DataFrame with only the important features
x_important = x[important_features]
x_important.info()
# Split data again with only the important features
x_train, x_validate, y_train, y_validate = train_test_split(x_important, y, test_size=0.3, random_state=42)

# Train a new Random Forest model with only the important features
rfc_important = RandomForestClassifier()
rfc_important.fit(x_train, y_train)
y_pred_important = rfc_important.predict(x_validate)
print("Random Forest Classifier (important features only):")
print(f"Confusion Matrix: \n{confusion_matrix(y_validate, y_pred_important)}")
print(f"F1 Score: {f1_score(y_validate, y_pred_important, average='macro', zero_division=0)}")
print(f"Accuracy: {accuracy_score(y_validate, y_pred_important)}")
print(f"Precision: {precision_score(y_validate, y_pred_important, average='macro', zero_division=0)}")
print()

# Save the trained model
joblib.dump(rfc_important, 'rfc_important_model.pkl')
joblib.dump(x_important.columns, 'important_features.pkl')