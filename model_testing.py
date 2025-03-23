import numpy as np
import pandas as pd

df = pd.read_csv("PythonWorks\PythonBasics\Datathon\\final_depression_dataset_1.csv")
df.dataframeName = 'final_depression_dataset_1.csv'

# Clean Data
df = df.drop(columns=["City", "Name", "Working Professional or Student", "Profession"])

# Convert "Depression" column from "Yes" or "No" to 1 and 0
df['Depression'] = df['Depression'].map({'Yes': 1, 'No': 0})

df.info()
df = pd.get_dummies(df)
# Check for NaN
df = df.fillna(df.mean())
df.info()

# Split data (80 train, 20 test)
from sklearn.model_selection import train_test_split
x = df.drop(columns=["Depression"]) # every column but "Depression and id"
y = df["Depression"].astype(int).values
x_train, x_validate, y_train, y_validate = train_test_split(x, y, test_size=0.2, random_state=42)

# Import validation measures
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

# Gaussian Naive Bayes 
from sklearn.naive_bayes import GaussianNB
gNB = GaussianNB()
#   train with training data
gNB.fit(x_train, y_train)
#   predict with x_validate
y_pred = gNB.predict(x_validate)
#   check validation measures
print("Gaussian Naive Bayes:")
print(f"Confusion Matrix: \n{confusion_matrix(y_validate, y_pred)}")
print(f"Accuracy: {accuracy_score(y_validate, y_pred)}")
print(f"F1 Score: {f1_score(y_validate, y_pred, average='macro', zero_division=0)}")
print(f"Precision: {precision_score(y_validate, y_pred, average='macro', zero_division=0)}")
print()

#K Nearest Neighbors
from sklearn import neighbors
models = []
#   Creates a KNN model for k = 1,3,5,7,9
#   Stores the models and the Accuracy Score in the list "models"
for k in range(1,10,2):
  clf = neighbors.KNeighborsClassifier(n_neighbors=k)
  clf.fit(x_train,y_train)
  y_pred = clf.predict(x_validate)
  models.append((accuracy_score(y_validate,y_pred),clf))
  print(f"K-Nearest-Neighbors: K = {k}")
  print(f"Confusion Matrix: \n{confusion_matrix(y_validate,y_pred)}")
  print(f"Accuracy: {accuracy_score(y_validate,y_pred)}")
  print(f"F1 Score: {f1_score(y_validate,y_pred,average = 'macro',zero_division=0)}")
  print(f"Precision: {precision_score(y_validate,y_pred,average = 'macro',zero_division=0)}")
  print()
#   Take the Model with the best Accuracy and predict with x_test
models = sorted(models, key = lambda x: -x[0]) #Sorts models based on accuracy score
clf = models[0][1]
y_pred = clf.predict(x_validate)
print("Best KNN:")
print(f"Confusion Matrix: \n{confusion_matrix(y_validate,y_pred)}")
print(f"F1 Score: {f1_score(y_validate,y_pred,average = 'macro',zero_division=0)}")
print(f"Accuracy: {accuracy_score(y_validate,y_pred)}")
print(f"Precision: {precision_score(y_validate,y_pred,average = 'macro',zero_division=0)}")
print()

#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_validate)
print("Random Forest Classifier:")
print(f"Confusion Matrix: \n{confusion_matrix(y_validate,y_pred)}")
print(f"F1 Score: {f1_score(y_validate,y_pred,average = 'macro',zero_division=0)}")
print(f"Accuracy: {accuracy_score(y_validate,y_pred)}")
print(f"Precision: {precision_score(y_validate,y_pred,average = 'macro',zero_division=0)}")
print()




