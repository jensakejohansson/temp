from calculator_helper import CalculatorHelper

class BaseTestCalculator():
    def setup_method(self, method):
        """setup any state tied to the execution of the given method in a
    class.  setup_method is invoked for every test method of a class."""
        self.calculator = CalculatorHelper()

    def teardown_method(self, method):
        """teardown any state that was previously setup with a setup_method
    call."""
        del self.calculator