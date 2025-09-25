import requests

class TestCalculatorAPI:
    url = "http://localhost:5000/calculate" 

    def test_multiplication(self):
        payload = {"operation": "multiply", "operand1": 3, "operand2": 4}
        response = requests.post(self.url, json=payload)
        assert response.status_code == 200
        assert response.json().get("result") == 12
    def test_division(self):
        payload = {"operation": "divide", "operand1": 10, "operand2": 2}
        response = requests.post(self.url, json=payload)
        assert response.status_code == 200
        assert response.json().get("result") == 5
    def test_addition(self):
        payload = {"operation": "add", "operand1": 5, "operand2": 7}
        response = requests.post(self.url, json=payload)
        assert response.status_code == 200
        assert response.json().get("result") == 12

