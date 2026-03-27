from pages.base_page import BasePage

from utils.role_helpers import click_role, fill_role
class LoginPage(BasePage):

    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BTN = "#login"

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def goto_login_page(self):
        self.visit("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        click_role(self.page, "button", "username")
        fill_role(self.page, "textbox", self.USERNAME, username)

