import pytest
import requests

class TestCalculatorAPI:
    def test_api(self):
        data = {"operation": "add", "operand1": 40, "operand2": 10}
        r = requests.post("http://localhost:5001/calculate", json=data)

        assert r.status_code == 200
        res = r.json()
        assert res["result"] == 50