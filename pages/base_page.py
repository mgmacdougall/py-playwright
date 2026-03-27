
class BasePage:
    def __init__(self, page):
        self.page = page

    def visit(self, url):
        self.page.goto(url, wait_until="networkidle")

    def click(self, locator):
        self.page.locator(locator).click()

    def type(self, locator, text):
        self.page.locator(locator).fill(text)

    def wait_for(self, locator):
        self.page.locator(locator).wait_for(state="visible")
