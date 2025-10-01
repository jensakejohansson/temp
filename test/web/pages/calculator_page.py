from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "user-name":  "#user-name",
            "key-1":  "#key-1",
            "key-2":  "#key-2",
            "key-add":  "#key-add",
            "key-subtract":  "#key-subtract",
            "key-multiply":  "#key-multiply",
            "key-divide":  "#key-divide",
            "key-equals":  "#key-equals",
            "calculator-screen":  "#calculator-screen",
            "toggle-button":  "#toggle-button",
            "history":  "#history",
            "logout":  "#logout-button",
        })

    def operations(self, operator):
        self.element("key-1").click()
        self.element(operator).click()
        self.element("key-2").click()
        self.element("key-equals").click()

    def check_history(self):
        self.operations("key-add")
        self.operations("key-multiply")
        self.element("toggle-button").click()
    
    def logout(self):
        self.element("logout").click()     

