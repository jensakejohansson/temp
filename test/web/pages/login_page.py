from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class LoginPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#username",
            "password": "#password",
            "password1": "#password1",
            "password2": "#password2",
            "login": "#login",
            "register": "#register",
        })

    def register(self, username, password1, password2):
        self.element("username").fill(username)
        self.element("password1").fill(password1)
        self.element("password2").fill(password2)
        self.element("register").click()
    
    def login(self, username, password):
        self.element("username").fill(username)
        self.element("password").fill(password)
        self.element("login").click()
        
