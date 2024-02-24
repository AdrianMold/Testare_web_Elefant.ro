from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium import webdriver


options = webdriver.ChromeOptions()


class SearchPage(BasePage):
    MAIN_PAGE_URL = "https://www.elefant.ro/"
    COOKIE_ACCEPT_BUTTON_ALL = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[name="SearchTerm"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.btn-search[type="submit"]')
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'div.search-result-headline')
    ELEFANT_LOGO = (By.CSS_SELECTOR, "img[alt='Logo']")
    PROMOTIONAL_BANNER = (By.CSS_SELECTOR, "img[alt='Slider GIGAsale']")
    STORE_FINDER_LINK = (By.CSS_SELECTOR, "a[href='https://www.elefant.ro/store-finder-map']")
    CATEGORY_BUTTON = (By.CSS_SELECTOR, "div.category-button")
    DELIVERY_PAGE = (By.CSS_SELECTOR, "#no-selection-overlay")
    ELECTRO_IT_LINK = (By.CSS_SELECTOR, "a[data-testing-id='Electro-link']")
    ELECTRONICS_IT_PRODUCTS = (By.CSS_SELECTOR, "h1.current-category-name")
    MONOPOLY_GAME_IMAGE = (By.CSS_SELECTOR, "img[alt='Joc Monopoly Pisici, in limba romana fotografia produsului']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-block.btn-primary.js-add-to-cart[name='addProduct']")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-primary.btn-lg.btn-block[href='https://www.elefant.ro/cart']")
    CART_HEADER = (By.CSS_SELECTOR, "div.cart-header")
    SHOPPING_CART_ICON = (By.XPATH, "//i[@class='material-icons' and text()='shopping_cart']")
    CANCEL_PRODUCT = (By.CSS_SELECTOR, "a.btn-tool.btn-delete i.material-icons")
    EMPTY_CART_MESSAGE = (By.XPATH, "//h2[text()='Nu există nici un produs în coș.']")
    NO_RESULT_FOUND = (By.XPATH, "//h1[@class='h2' and contains(text(), 'Nu a fost găsit nici un rezultat :')]")

    '''Scenariu 2'''
    def navigate_to_main_page(self):
        self.chrome.get(self.MAIN_PAGE_URL)


    def accept_cookies1(self):
        WebDriverWait(self.chrome, 10).until(EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON_ALL)).click()


    def enter_book_name(self):
        book_name = "Harry Potter"
        self.type(self.SEARCH_INPUT, book_name)


    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)


    def is_book_list_displayed(self, book_name):
        try:
            search_results_element = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.SEARCH_RESULTS))

            return book_name in search_results_element.text
        except TimeoutException:
            return False

    def is_specific_book_displayed(self, book_name):
        try:
            WebDriverWait(self.chrome, 15).until(EC.visibility_of_element_located(self.SEARCH_RESULTS))
            return True
        except NoSuchElementException:
            return False


    '''Scenariu 4'''
    def is_logo_present(self):
        try:
            WebDriverWait(self.chrome, 15).until(EC.visibility_of_element_located(self.ELEFANT_LOGO))
            return True
        except NoSuchElementException:
            return False

    '''Scenariu 5'''
    def is_banner_present(self):
        try:
            WebDriverWait(self.chrome, 15).until(EC.visibility_of_element_located(self.PROMOTIONAL_BANNER))
            return True
        except NoSuchElementException:
            return False

    def is_banner_present_click(self):
        try:
            banner = self.chrome.find_element(*self.PROMOTIONAL_BANNER)
            banner.click()
            return True
        except NoSuchElementException:
            return False

    '''Scenariu 6'''
    def location_point_click(self):
        try:
            deliver_location = WebDriverWait(self.chrome, 10).until(
                EC.element_to_be_clickable(self.STORE_FINDER_LINK))
            deliver_location.click()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def location_point_displayed(self):
        try:
            WebDriverWait(self.chrome, 15).until(EC.visibility_of_element_located(self.DELIVERY_PAGE))
            return True
        except NoSuchElementException:
            return False

    '''Scenariu 7'''
    def category_button_click(self):
        try:
            menu_button = self.chrome.find_element(*self.CATEGORY_BUTTON)
            menu_button.click()
            return True
        except NoSuchElementException:
            return False

    def electro_it_link(self):
        try:
            electro_it = self.chrome.find_element(*self.ELECTRO_IT_LINK)
            electro_it.click()
            return True
        except NoSuchElementException:
            return False

    def are_electronics_it_products_displayed(self):
        try:
            self.chrome.find_elements(*self.ELECTRONICS_IT_PRODUCTS)
            return True
        except NoSuchElementException:
            return False

    '''Scenariu 8'''
    def enter_game_name(self, game_name):
        game_name = "Joc Monopoly"
        self.type(self.SEARCH_INPUT, game_name)

    def is_game_list_displayed(self, game_name):
        try:
            search_game_results = WebDriverWait(self.chrome, 15).until(
                EC.visibility_of_element_located(self.SEARCH_RESULTS)
            )
            assert game_name in search_game_results.text
        except TimeoutException:
            assert False

    def monopoly_game(self):
        try:
            monopoly = self.chrome.find_element(*self.MONOPOLY_GAME_IMAGE)
            monopoly.click()
            return True
        except NoSuchElementException:
            return False

    def monopoly_add_to_cart(self):
        try:
            monopoly_cart = self.chrome.find_element(*self.ADD_TO_CART_BUTTON)
            monopoly_cart.click()
            return True
        except NoSuchElementException:
            return False

    def cart_is_displayed(self):
        try:
            cart = self.chrome.find_element(*self.VIEW_CART_BUTTON)
            cart.click()
            return True
        except NoSuchElementException:
            return False

    '''Scenariu 9'''
    def navigate_and_verify_shopping_cart(self):
        try:
            WebDriverWait(self.chrome, 15).until(
                EC.element_to_be_clickable(self.SHOPPING_CART_ICON)
            )
            cart_button = self.chrome.find_element(*self.SHOPPING_CART_ICON)
            cart_button.click()

            view_cart = self.chrome.find_element(*self.VIEW_CART_BUTTON)
            view_cart.click()
            return True
        except NoSuchElementException:
            return False

    def cancel_product(self):
        try:
            product = WebDriverWait(self.chrome, 15).until(
        EC.element_to_be_clickable(self.CANCEL_PRODUCT))
            product.click()
            return True
        except NoSuchElementException:
            return False

    def removed_product_displayed(self):
        try:
            WebDriverWait(self.chrome, 15).until(
                EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE))
            return True
        except NoSuchElementException:
            return False

    '''Scenariu 10'''
    def special_characters_search(self, special_characters):
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(special_characters)

    def no_results(self):
        no_result_element = self.chrome.find_element(*self.NO_RESULT_FOUND)
        assert no_result_element.is_displayed() #, "No results message not displayed"
















