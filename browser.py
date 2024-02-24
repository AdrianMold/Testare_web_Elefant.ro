from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Browser:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    #chrome = webdriver.Chrome(service=service, options=options)
    chrome = webdriver.Chrome(service=service)
    chrome.maximize_window()
    chrome.implicitly_wait(10)

    def close(self):
        self.chrome.quit()


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

















