from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#user-name",
            "1": "#key-1",
            "add": "#key-add",
            "subtract": "#key-subtract",
            "multiply": "#key-multiply",
            "divide": "#key-divide",
            "equals": "#key-equals",
            "calculator_screen": "#calculator-screen",
            "toggle_history": "#toggle-button",
            "text_window": "#text-window",
            "text_area": "#history",
            "logout": "#logout-button",
        })

    def add(self):
        self.element("1").click()
        self.element("add").click()
        self.element("1").click()
        self.element("equals").click()

    def subtract(self):
        self.element("1").click()
        self.element("subtract").click()
        self.element("1").click()
        self.element("equals").click()

    def multiply(self):
        self.element("1").click()
        self.element("multiply").click()
        self.element("1").click()
        self.element("equals").click()
    
    def divide(self):
        self.element("1").click()
        self.element("divide").click()
        self.element("1").click()
        self.element("equals").click()




