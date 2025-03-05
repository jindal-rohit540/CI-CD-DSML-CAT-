import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Load the model
with open("random_forest.pkl", 'rb') as model_pickle:
    clf = pickle.load(model_pickle)

app = Flask(__name__)

# Define the prediction function
@app.route('/predict', methods=['POST'])
def prediction():
    # Pre-processing user input
    loan_req = request.get_json()
    print(loan_req)  

    # Convert categorical values to numerical
    Gender = 0 if loan_req.get('Gender') == "Male" else 1
    Married = 0 if loan_req.get('Married') == "Unmarried" else 1
    Credit_History = 0 if loan_req.get('Credit_History') == "Unclear Debts" else 1  

    ApplicantIncome = loan_req.get('ApplicantIncome', 0)
    LoanAmount = loan_req.get('LoanAmount', 0) / 1000  

    # Create DataFrame with proper feature names
    input_df = pd.DataFrame([{
        'Gender': Gender,
        'Married': Married,
        'ApplicantIncome': ApplicantIncome,
        'LoanAmount': LoanAmount,
        'Credit_History': Credit_History
    }])

    # Making predictions  
    prediction = clf.predict(input_df)

    pred = 'Rejected' if prediction[0] == 0 else 'Approved'

    return jsonify({'loan_approval_status': pred})

# Health check endpoint
@app.route('/ping', methods=['GET'])
def ping():
    return "Pinging Model!!"

if __name__ == '__main__':
    app.run(debug=True)  # Debug mode for better error messages
