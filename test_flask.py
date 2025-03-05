import pytest
from app import app
import json



@pytest.fixture
def client():
    return app.test_client()


## Function to test home page end point
def test_ping(client):
    resp = client.get('/ping')
    assert resp.status_code == 200

# test predict end point 
def test_predict(client):
    test_data={'Gender':"Male", 'Married':"Unmarried",'Credit_History' : "Unclear Debts",'ApplicantIncome':100000,'LoanAmount':2000000}

    response = client.post('/predict', json = test_data)

    assert response.status_code == 200
    assert response.json == {'loan_approval_status': 'Approved'}
