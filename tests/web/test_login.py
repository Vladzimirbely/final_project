from final_project.pages.login_page import LoginPage
import allure

login_page = LoginPage()

@allure.epic('Login')
@allure.story('Login user with correct data')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_successfull_login_user():
    login_page.open()
    login_page.login_user_with_correct_data()
    login_page.should_successfull_login()

@allure.epic('Login')
@allure.story('Login user with incorrect data')
@allure.feature('Login')
@allure.tag('web')
@allure.label('owner')
@allure.severity('high')
def test_unsuccessfull_login_user():
    login_page.open()
    login_page.login_user_with_incorrect_data()
    login_page.should_unsuccessfull_login()
