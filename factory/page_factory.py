class PageFactory:

    def __init__(self, page):
        self.page = page

    @property
    def login(self):
        from pages.login_page import LoginPage

        return LoginPage(self.page)

    @property
    def dashboard(self):
        from pages.dashboard_page import DashboardPage

        return DashboardPage(self.page)

    @property
    def add_remove(self):
        from pages.add_remove import AddRemove

        return AddRemove(self.page)

    @property
    def drop_down(self):
        from pages.drop_down import DropDown

        return DropDown(self.page)