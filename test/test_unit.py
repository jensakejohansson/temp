import pytest
from test_base import BaseTestCalculator

class TestCalculator(BaseTestCalculator):

    @pytest.mark.parametrize(
            "a, b, expected",
            [
                (3, 3, 6), 
                (2, -2, 0), 
                (28, 34, 62), 
                (-2, -2, -4)
            ]
    )
  
    def test_add(self, a, b, expected):
        value = self.calculator.add(a, b)
        assert value == expected

    @pytest.mark.parametrize(
            "a, b, expected",
            [
                (150, 50, 100), 
                (5, 3, 2), 
                (3, 3, 0), 
                (0, 4, -4)
            ]
    )
  
    def test_subtract(self, a, b, expected):
        value = self.calculator.subtract(a, b)
        assert value == expected

    @pytest.mark.parametrize(
            "a, b, expected",
            [
                (2, 3, 6), 
                (4, 4, 16), 
                (-2, 4, -8), 
                (30, 3, 90)
            ]
    )
  
    def test_multiply(self, a, b, expected):
        value = self.calculator.multiply(a, b)
        assert value == expected

    @pytest.mark.parametrize(
            "a, b, expected",
            [
                (6, 3, 2), 
                (5, 2, 2.5), 
                (10, 2, 5)
            ]
    )
  
    def test_divide(self, a, b, expected):
        value = self.calculator.divide(a, b)
        assert value == expected

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0