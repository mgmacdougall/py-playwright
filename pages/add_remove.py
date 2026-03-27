from pages.base_page import BasePage

class AddRemove(BasePage):

    header = "h3"


    def is_loaded(self):
        # TODO: Replace with real locator
        return True
    
    def goto_add_remove_page(self):
        self.visit("https://the-internet.herokuapp.com/add_remove_elements/")
    
    def click_add_element(self):
        self.click("button[onclick='addElement()']")

    def get_element_count(self):
        return self.page.locator("div#elements button").count()
    
    def get_page_header(self):
        return self.page.locator(self.header).inner_text()

    def remove_element(self):
        self.click("div#elements button")
    
    def remove_element_by_place(self, place):
        self.page.locator("div#elements button").nth(place).click()
        
    def get_element_count_after_removal(self):
        return self.page.locator("div#elements button").count()