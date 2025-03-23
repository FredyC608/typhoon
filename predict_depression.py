import pandas as pd
import joblib


'''

This function takes in a list of user inputs and returns a prediction of whether the user is depressed or not.
The list contain values in the following order:

['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction',
'Have you ever had suicidal thoughts ?', 'Work/Study Hours', 'Financial Stress']
'''
def predict_depression(user_input):
    # Convert input list to dictionary
    user_input_dict = {
        'Age': user_input[0],
        'Academic Pressure': user_input[1],
        'Work Pressure': user_input[2],
        'CGPA': user_input[3],
        'Study Satisfaction': user_input[4],
        'Job Satisfaction': user_input[5],
        'Have you ever had suicidal thoughts ?': user_input[6],
        'Work/Study Hours': user_input[7],
        'Financial Stress': user_input[8]
    }
    
    # Load the trained model and important features
    rfc_important = joblib.load('rfc_important_model.pkl')
    important_features = joblib.load('important_features.pkl')

    # Convert user input to DataFrame
    user_df = pd.DataFrame([user_input_dict])
    
    # Convert CGPA from 4.0 scale to 10.0 scale
    user_df['CGPA'] = user_df['CGPA'] * 2.5

    # Apply the same get_dummies transformation to the user input
    user_df = pd.get_dummies(user_df)

    # Ensure the user input DataFrame has the same columns as the important features
    user_df = user_df.reindex(columns=important_features, fill_value=0)

    # Predict depression for the user input
    user_pred = rfc_important.predict(user_df)
    return user_pred[0]

# Example usage
# if __name__ == "__main__":
#     user_input = [
#         25, 3, 2, 3.5, 4, 3, 'No', 6, 2
#     ]
#     prediction = predict_depression(user_input)
#     print(f"Predicted Depression: {prediction}")
