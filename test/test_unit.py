from BE.calculator_helper import CalculatorHelper
import pytest
from test.test_base import BaseTest

#from assertpy import assert_that
#inherit

class TestCalculator(BaseTest):

    def test_first(self):
        pass
    def test_add(self):
        # Act
        result = self.calculator.add(1, 1)
        # Assert
        assert result == 2

    @pytest.mark.parametrize(
            "a, b, expected",
            [
                (3, 3, 0),
                (1, 1, 0),
                (2, 1, 1),
                (2, -2, 4),
                (-4, 2, -6),         
            ]
    )
    def test_subtract(self, a, b, expected):
        result = self.calculator.subtract(a, b)
        assert result == expected
    def test_multiply(self):
        result = self.calculator.multiply(1, 1)
        assert result == 1
    def test_divide_error(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(1, 0)
    def test_divide(self):
        result = self.calculator.divide(4,2)
        assert result == 2
        #assert_that(result).is_equal_to(2)
