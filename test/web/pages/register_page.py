from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class RegisterPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#username",
            "password":  "#password1",
            "password2":  "#password2",
            "register":  "#register",
            "logout":  "#logout-button",
        })

    def register(self, username, password1, password2):
        self.element("register").click()
        self.element("username").fill(username)
        self.element("password").fill(password1)
        self.element("password2").fill(password2)
        self.element("register").click()
