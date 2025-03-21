import pytest
import json

from app import app


## Mimicing like the server and fetching the response
@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resposne = client.get('/ping')
    assert resposne.status_code == 200


def test_predict(client):
    ## Give some data
    test_data = {'Gender':"Male", 'Married':"Unmarried",'Credit_History' : "Unclear Debts",'ApplicantIncome':100000,'LoanAmount':2}
    ## Capture the response 

    response = client.post('/predict', json = test_data)

    ## Assert whether repson. status code  = 200
    assert response.status_code == 200
    assert response.json=={'loan_approval_status': 'Approved'}
