import pandas as pd
import joblib

def predict_depression(user_input):
    # Load the trained model and important features
    rfc_important = joblib.load('rfc_important_model.pkl')
    important_features = joblib.load('important_features.pkl')

    # Convert user input to DataFrame
    user_df = pd.DataFrame([user_input])

    # Apply the same get_dummies transformation to the user input
    user_df = pd.get_dummies(user_df)

    # Ensure the user input DataFrame has the same columns as the important features
    user_df = user_df.reindex(columns=important_features, fill_value=0)

    # Predict depression for the user input
    user_pred = rfc_important.predict(user_df)
    return user_pred[0]

# # Example usage
# if __name__ == "__main__":
#     user_input = {
#         'Age': 25,
#         'Academic Pressure': 3,
#         'Work Pressure': 2,
#         'CGPA': 7.5,
#         'Study Satisfaction': 4,
#         'Job Satisfaction': 3,
#         'Have you ever had suicidal thoughts ?': 'No',
#         'Work/Study Hours': 6,
#         'Financial Stress': 2
#     }
#     prediction = predict_depression(user_input)
#     print(f"Predicted Depression: {prediction}")
