from behave import *

#------------------Scenariu 2------------------------


@given('We are on the main page of www.elefant.ro')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@when('I enter "{book_name}" in the search bar')
def step_impl(context, book_name):
    context.main_page.enter_book_name()

@when('I click on the search button')
def step_impl(context):
    context.main_page.click_search_button()

@then('I should receive a list of "{book_name}" books')
def step_impl(context, book_name):
    context.main_page.is_book_list_displayed(book_name)


#------------------Scenariu 4-----------------------

@given('I am on the main page of www.elefant.ro')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@then('the elefant.ro logo should be present')
def step_impl(context):
    context.main_page.is_logo_present()


#--------------------Scenariu 5----------------------

@given('You are on the main page of www.elefant.ro')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@when('A promotional banner should be displayed')
def step_iml(context):
    context.main_page.is_banner_present()

@then('Click on the promotional banner')
def step_impl(context):
    context.main_page.is_banner_present_click()


#--------------------Scenariu 6---------------------

@given('User is on the main page')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@when('User clicks on the "Puncte Livrare" link')
def step_impl(context):
    context.main_page.location_point_click()

@then('User should be on the Puncte Livrare page')
def step_impl(context):
    context.main_page.location_point_displayed()


#------------------Scenariu 7----------------------------

@given('User1 on the main page of www.elefant.ro')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@when('User1 clicks the "Categorii"')
def step_impl(context):
    context.main_page.category_button_click()

@when('User1 navigates through the menu to "Electronice & IT"')
def step_impl(context):
    context.main_page.electro_it_link()

@then('User1 should see products related to "Electronice & IT"')
def step_impl(context):
    context.main_page.are_electronics_it_products_displayed()


#------------------Scenariu 8-------------------------

@given('User2 is on the main page of www.elefant.ro')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@when('User2 searches for "{game_name}" in the search bar')
def step_impl(context, game_name):
    context.main_page.enter_game_name(game_name)

@when('User2 clicks on the search button')
def step_impl(context):
    context.main_page.click_search_button()

@when('User2 reveives a list of "{game_name}" games')
def step_impl(context, game_name):
    context.main_page.is_game_list_displayed(game_name)

@when('User2 selects the first product from the search results')
def step_impl(context):
    context.main_page.monopoly_game()

@when('User2 adds the product to the shopping cart')
def step_impl(context):
    context.main_page.monopoly_add_to_cart()

@then("The product should be in User2's shopping cart")
def step_impl(context):
    context.main_page.cart_is_displayed()


#-------------------Scenariu 9-------------------------

@given('User3 is on the main page of www.elefant.ro')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@when('User3 navigates to the shopping cart')
def step_impl(context):
    context.main_page.navigate_and_verify_shopping_cart()

@when('User3 clicks the "Remove" button for a specific product')
def step_impl(context):
    context.main_page.cancel_product()

@then('The product should be removed from the shopping cart')
def step_impl(context):
    context.main_page.removed_product_displayed()


#--------------------Scenariu 10-------------------------------

@given('User4 is on the main page of www.elefant.ro')
def step_impl(context):
    context.main_page.navigate_to_main_page()

@when('User4 types special characters "{special_characters}" into the search bar and presses the search button')
def step_impl(context, special_characters):
    context.main_page.special_characters_search(special_characters)
    context.main_page.click_search_button()

@then('An appropriate message indicating no results should be displayed')
def step_impl(context):
    context.main_page.no_results()


























