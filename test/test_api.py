import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse

class TestCalculatorAPI():
    def test_add_example(self):
        #arrange
        url = "http://localhost:5000/calculate"
        payload = {
            "operation": "add",
            "operand1": 55,
            "operand2": 365
        }
        #act
        response = requests.post(url, json=payload)
        #assert
        #response is a JSON object & needs to be "decoded"
        assert response.json()["result"] == 420
    
    def test_add_api(self):
        client = Client("http://localhost:5000")
        #sync: we send smth to calculate api endpoint & wait for response b4 continuing execution
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1 = 1, operand2 = 2))
        assert isinstance(response, ResultResponse)
        assert response.result == 3
    
    def test_subtract_api(self):
        client = Client("http://localhost:5000")
        #sync: we send smth to calculate api endpoint & wait for response b4 continuing execution
        response = calculate.sync(client = client, body = Calculation(Opertions.SUBTRACT, operand1 = 1, operand2 = 2))
        assert isinstance(response, ResultResponse)
        assert response.result == -1
    
    def test_multiply_api(self):
        client = Client("http://localhost:5000")
        #sync: we send smth to calculate api endpoint & wait for response b4 continuing execution
        response = calculate.sync(client = client, body = Calculation(Opertions.MULTIPLY, operand1 = 73, operand2 = 235))
        assert isinstance(response, ResultResponse)
        assert response.result == 17155
    
    def test_divide_api(self):
        client = Client("http://localhost:5000")
        #sync: we send smth to calculate api endpoint & wait for response b4 continuing execution
        response = calculate.sync(client = client, body = Calculation(Opertions.DIVIDE, operand1 = 15, operand2 = 3))
        assert isinstance(response, ResultResponse)
        assert response.result == 5

#move client = ... into setup girl