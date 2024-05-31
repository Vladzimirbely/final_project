import pytest
from rabotaby_project_tests.pages.login_page import login_page
import allure


@allure.epic('Login')
@allure.story('Login user with correct data')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
@pytest.mark.web
@pytest.mark.critical
@allure.title('Successfully login')
def test_successfully_login_user():
    login_page.open()
    login_page.login_user_with_correct_data()
    login_page.should_successfully_login()


@allure.epic('Login')
@allure.story('Login user with incorrect data')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
@pytest.mark.web
@pytest.mark.critical
@allure.title('Unsuccessfully login')
def test_unsuccessfully_login_user():
    login_page.open()
    login_page.login_user_with_incorrect_data()
    login_page.should_unsuccessfully_login()
