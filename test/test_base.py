from BE.calculator_helper import CalculatorHelper

class BaseTest:

    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        cls.calculator = CalculatorHelper()


    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to
        setup_class.
        """
        cls.calculator = None
