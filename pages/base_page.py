from browser import Browser

class BasePage(Browser):

    def find(self, locator):
        return self.chrome.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()















