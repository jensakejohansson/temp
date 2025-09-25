
from BE.calculator_helper import CalculatorHelper


class TestCalculator:
    def test_first(self):
        caluclator = CalculatorHelper()
        assert caluclator.add(1, 2) == 3
