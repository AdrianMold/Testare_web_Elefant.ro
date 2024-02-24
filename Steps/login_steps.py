from behave import *

#-----------------Scenariu 1---------------------------


@given('We are on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when('I have accepted cookies')
def step_impl(context):
    context.login_page.accept_cookies()

@when('I enter the email address "{email}"')
def step_impl(context, email):
    context.login_page.fill_in_email(email)

@when('I enter password {password}')
def step_impl(context, password):
    context.login_page.fill_in_password(password)

@when('I press the login button')
def step_impl(context):
    context.login_page.press_loggin_button()

@then('I should be logged in with my email address')
def step_impl(context):
    context.login_page.is_logged_in()


#--------------------Scenariu 3---------------------------

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when('I log out')
def step_impl(context):
    context.login_page.logout_if_logged_in()

@when('I navigate back on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when('I fill in with wrong email')
def step_impl(context):
    context.login_page.fill_in_wrong_email()

@when('I fill in with wrong password')
def step_impl(context):
    context.login_page.fill_in_wrong_password()

@when('I click the login button')
def step_impl(context):
    context.login_page.press_loggin_button()


@then('I should see an error message')
def step_impl(context):
    context.login_page.is_error_message_displayed()













