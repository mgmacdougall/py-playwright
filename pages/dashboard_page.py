from pages.base_page import BasePage


class DashboardPage(BasePage):

    HEADER = "h1"

    def assert_loaded(self):
        self.wait_for(self.HEADER)

    def true_is_true(self):
        return True
