from test.web.test_base import WebBase
from playwright.sync_api import expect  
from test.web.pages.login_page import LoginPage
from test.web.pages.calculator_page import CalculatorPage
import pytest

#on loginpage, defined element looks at login_page and action fill

class TestWeb(WebBase):

    def test_register(self):
        LoginPage(self.page).element("register").click()
        LoginPage(self.page).register("admin4", "test123", "test123")
        expect(CalculatorPage(self.page).element("username")).to_have_text("admin4")

    def test_add(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).add()
        expect(CalculatorPage(self.page).element("calculator_screen")).to_have_value("2")
    
    def test_subtract(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).subtract()
        expect(CalculatorPage(self.page).element("calculator_screen")).to_have_value("0")

    def test_multiply(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).multiply()
        expect(CalculatorPage(self.page).element("calculator_screen")).to_have_value("1")

    def test_divide(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).divide()
        expect(CalculatorPage(self.page).element("calculator_screen")).to_have_value("1")

    def test_verify(self):
        LoginPage(self.page).login("admin", "test1234")
        CalculatorPage(self.page).add()
        CalculatorPage(self.page).element("toggle_history").click()
        expect(CalculatorPage(self.page).element("text_area")).to_have_value("1+1=2\n")



