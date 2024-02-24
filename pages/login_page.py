from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium import webdriver
import time

options = webdriver.ChromeOptions()


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://www.elefant.ro/login"
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[placeholder="Email"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Parola"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block[name="login"]')
    COOKIE_ACCEPT_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    LOGGED_IN_ELEMENT = (By.CSS_SELECTOR, 'h2')
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-danger[role='alert']")
    ELEMENT = (By.CSS_SELECTOR, 'span.hidden-xs.login-name')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.my-account-logout")

    '''Scenariu 1'''
    def navigate_to_login_page(self):
        self.chrome.get(self.LOGIN_PAGE_URL)

    def accept_cookies(self):
        WebDriverWait(self.chrome, 10).until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)).click()

    def fill_in_email(self, email):
        email = "alaaabalaaa3@yahoo.com"
        self.chrome.find_element(*self.INPUT_EMAIL).send_keys(email)

    def fill_in_password(self, password):
        password = "portocala"
        self.chrome.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def press_loggin_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return self.is_displayed(self.LOGGED_IN_ELEMENT)

    '''Scenariu 3'''
    def logout_if_logged_in(self):
        try:
            element_button = self.chrome.find_element(*self.ELEMENT)
            element_button.click()
            WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
        except NoSuchElementException:
            return False

        try:
            logout_button = self.chrome.find_element(*self.LOGOUT_BUTTON)
            logout_button.click()
            return True
        except NoSuchElementException:
            return False

    def fill_in_wrong_email(self):
        WebDriverWait(self.chrome, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Email"]'))
        )
        email2 = 'email@yahoo.com'
        self.chrome.find_element(*self.INPUT_EMAIL).send_keys(email2)

    def fill_in_wrong_password(self):
        password2 = '123456'
        self.chrome.find_element(*self.INPUT_PASSWORD).send_keys(password2)

    def is_error_message_displayed(self):
        try:
            WebDriverWait(self.chrome, 15).until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return True
        except NoSuchElementException:
            return False





