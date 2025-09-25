import requests
from test.calculator_client.client import Client
from test.calculator_client.api.actions import calculate
from test.calculator_client.models.calculation import Calculation
from test.calculator_client.models.opertions import Opertions
from test.calculator_client.models import ResultResponse
import pytest


class TestCalculatorAPI():                         
    def test_add_api(self):
        url = "http://localhost:5001/calculate"
        payload = {
            "operation": "add",
            "operand1": 5,
            "operand2": 5
        }
        response = requests.post(url, json=payload)
        a = response.json()
        assert a["result"] == 10

    def test_generated_code_add(self):
        client = Client("http://localhost:5001")
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result == 3

    def test_generated_code_subtract(self):
        client = Client("http://localhost:5001")
        response = calculate.sync(client = client, body = Calculation(Opertions.SUBTRACT, operand1=1, operand2=2))
        # ResultResponse object
        assert isinstance(response, ResultResponse)
        assert response.result == -1

    def test_generated_code_multiply(self):
        client = Client("http://localhost:5001")
        response = calculate.sync(client = client, body = Calculation(Opertions.MULTIPLY, operand1=1, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result == 2

