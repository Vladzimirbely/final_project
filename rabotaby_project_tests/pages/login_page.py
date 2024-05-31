import os
from selene import browser, have
import allure


class LoginPage:
    def open(self):
        with allure.step('Open browser'):
            browser.open('')
            return self

    def login_user_with_correct_data(self):
        with allure.step('Click on login button'):
            browser.element('[data-qa=login]').click()
        with allure.step('Click on login with password button'):
            browser.element('[data-qa=expand-login-by-password]').click()
        with allure.step('Enter login'):
            browser.element('[data-qa=login-input-username]').type(os.getenv('user_login'))
        with allure.step('Enter password'):
            browser.element('[data-qa=login-input-password]').type(os.getenv('user_password'))
        with allure.step('Click on submit button'):
            browser.element('[data-qa=account-login-submit]').click()

    def should_successfully_login(self):
        with allure.step('Click on profile button'):
            browser.element('[data-qa=mainmenu_applicantProfile]').click()
        with allure.step('Checking username'):
            browser.element('[data-qa=mainmenu_applicantInfo]').should(have.text('Владимир Белый'))

    def login_user_with_incorrect_data(self):
        with allure.step('Click on login button'):
            browser.element('[data-qa=login]').click()
        with allure.step('Click on login with password button'):
            browser.element('[data-qa=expand-login-by-password]').click()
        with allure.step('Enter incorrect login'):
            browser.element('[data-qa=login-input-username]').type('qwerty')
        with allure.step('Enter incorrect password'):
            browser.element('[data-qa=login-input-password]').type('asasdasd')
        with allure.step('Click on submit button'):
            browser.element('[data-qa=account-login-submit]').click()

    def should_unsuccessfully_login(self):
        with allure.step('Checking error message'):
            browser.element('[data-qa=account-login-error]').should(
                have.text('Неправильные данные для входа. Пожалуйста, попробуйте снова.'))


login_page = LoginPage()
