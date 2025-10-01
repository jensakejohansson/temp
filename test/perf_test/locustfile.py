from locust import HttpUser, task, between
import json
import random

class CalculatorUser(HttpUser):

    wait_time = between(2,4) #secs in between tasks

    def on_start(self):
        pass

    @task(2) #makes its execution twice as likely as any other operation
    def add(self):
        data = [[1,1,2],[2,4,6]]
        data_to_use = random.choice(data)
        add = {
            "operation": "add",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")
        
    
    @task
    def subtract(self):
        data = [[1,1,0],[2,4,-2]]
        data_to_use = random.choice(data)
        subtract = {
            "operation": "subtract",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=subtract) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")

    @task
    def multiply(self):
        data = [[1,1,1],[2,4,8]]
        data_to_use = random.choice(data)
        multiply = {
            "operation": "multiply",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=multiply) as response:
            response_data = json.loads(response.text)
            #print("AAAAAAAAAAAAAAAAAAA" + response.text)
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")

    @task
    def divide(self):
        data = [[1,1,1],[4,2,2]]
        data_to_use = random.choice(data)
        divide = {
            "operation": "divide",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=divide) as response:
            response_data = json.loads(response.text)
            #print(response_data)
            if 'result' not in response_data:
                response.failure(f"Missing result key in response: {response_data}")
            else:
                if not response_data['result'] == data_to_use[2]:
                    response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")
            


if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
