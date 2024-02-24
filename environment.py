'''
1. cream fisierul browser
2. cream fisierul environment si in context pune Browser
3. cream fisierul features unde detaliem scenariile de test
4. cand stim scenariile, stim pasii deci cream fisierul steps
5. dupa ce am creat pasii cream pagina, cu elemente si metode
6. revenim la fisierul environment si adaugam pagina in context
'''
from selenium.webdriver.chrome import webdriver
from browser import Browser
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from selenium import webdriver


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.main_page = SearchPage()

def after_all(context):
    context.browser.close()

# obiectele din environment mapeaza paginile web












