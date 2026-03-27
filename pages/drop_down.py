from pages.base_page import BasePage

class DropDown(BasePage):

    def is_loaded(self):
        # TODO: Replace with real locator
        return True

    def get_page_header(self):
        return self.page.locator("h3").inner_text()
    
    def goto_drop_down_page(self):
        self.visit("https://the-internet.herokuapp.com/dropdown")   

    def get_all_options(self):
        options = self.page.locator("select#dropdown option")
        return [options.nth(i).inner_text() for i in range(options.count())]
    
    def select_option_by_text(self, text):
        self.page.select_option("select#dropdown", label=text)