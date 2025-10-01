import pytest
from BE.calculator_helper import CalculatorHelper

class Base():

    # no @classmethod bc we only want an instance of the class NOT the class itself
    def setup_method(self, method):
        self.calculator = CalculatorHelper()

    def teardown_method(self, method):
        del self.calculator
        

class TestCalculator(Base):
    def test_add(self):
        #arrange is done in the setup method
        value = self.calculator.add(1,1)
        assert value == 2, "I expect you to know this"

    #essentially jsut define a set of parameters that will be tested
    @pytest.mark.parametrize("a, b, expected", [(9,3,6),(5,1,4),(20,9,11)])
    def test_subtract(self, a, b, expected):
        value = self.calculator.subtract(a,b)
        assert value == expected, "Something ain't right"
    
    def test_multiply(self):
        value = self.calculator.multiply(2,3)
        assert value == 6
    
    def test_divide(self):
        value = self.calculator.divide(12,3)
        assert value == 4
    
    def test_zero_division(self):
        #tells pytest that we expect ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            #tests divide method in case of 1/0
            self.calculator.divide(1,0)
            #look up try/catch
