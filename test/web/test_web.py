from test.web.test_base import WebBase
from test.web.pages.login_page import LoginPage
from test.web.pages.register_page import RegisterPage
from test.web.pages.calculator_page import CalculatorPage
from playwright.sync_api import expect
import pytest

class TestWeb(WebBase):
    def test_login(self):
        #self.page: comms between code & browser
        LoginPage(self.page).login("admin", "test1234")
        expect(CalculatorPage(self.page).element("user-name")).to_have_text("admin")
        CalculatorPage(self.page).logout()

    def test_add(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).operations("key-add")
        expect(CalculatorPage(self.page).element("calculator-screen")).to_have_value("3")
        CalculatorPage(self.page).logout()
    
    def test_subtract(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).operations("key-subtract")
        expect(CalculatorPage(self.page).element("calculator-screen")).to_have_value("-1")
        CalculatorPage(self.page).logout()
    
    def test_multiply(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).operations("key-multiply")
        expect(CalculatorPage(self.page).element("calculator-screen")).to_have_value("2")
        CalculatorPage(self.page).logout()
        
    def test_divide(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).operations("key-divide")
        expect(CalculatorPage(self.page).element("calculator-screen")).to_have_value("0.5")
        CalculatorPage(self.page).logout()    

    def test_registration(self):
        RegisterPage(self.page).register("Lin Manual Miranda", "1234", "1234")
        expect(CalculatorPage(self.page).element("user-name")).to_have_text("Lin Manual Miranda")
        CalculatorPage(self.page).logout()

    def test_history(self):
        LoginPage(self.page).login("snoopy", "1234")
        CalculatorPage(self.page).check_history()
        expect(CalculatorPage(self.page).element("history")).to_have_value("1+2=3\n1*2=2\n")
        CalculatorPage(self.page).logout()    

#indiviudalize tests & randomize registration input through randomint(1,9999)
