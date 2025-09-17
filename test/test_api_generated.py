from calculator_client.client import Client
from calculator_client.models.calculation import Calculation
from calculator_client.api.actions import calculate
from calculator_client.models.result_response import ResultResponse
from calculator_client.models.calculation import Opertions

#Arrange
base_url="http://localhost:5001"
client = Client(base_url)

def test_add():
    
    # Arrange
    calc_add = Calculation(
        operation=Opertions.ADD,
        operand1=40,
        operand2=10
    )
    
    # Act
    result_add: ResultResponse = calculate.sync(client=client, body=calc_add)
    
    # Assert
    assert result_add.result == 50



calc_subtract = Calculation(
    operation=Opertions.SUBTRACT,
    operand1=40,
    operand2=10
)

calc_multiply = Calculation(
    operation=Opertions.MULTIPLY,
    operand1=1000,
    operand2=10
)

calc_divide = Calculation(
    operation=Opertions.DIVIDE,
    operand1=50,
    operand2=10
)



result_subtract: ResultResponse = calculate.sync(client=client, body=calc_subtract)
print(result_subtract.result)

result_multiply: ResultResponse = calculate.sync(client=client, body=calc_multiply)
print(result_multiply.result)

result_divide: ResultResponse = calculate.sync(client=client, body=calc_divide)
print(result_divide.result)