import os
import allure
from dotenv import load_dotenv
from jsonschema import validate
from rabotaby_project_tests.utils.load_json import load_json
from rabotaby_project_tests.utils.api_helper import api_request


@allure.epic('Login')
@allure.story('Login user with correct data')
@allure.feature('Login')
@allure.tag('API')
@allure.label('owner')
@allure.severity('high')
def test_login_with_correct_data(base_api_url):
    load_dotenv()

    login = os.getenv('user_login_api')
    password = os.getenv('user_password_api')
    endpoint = '/account/login'

    params = {'username': login, 'password': password, 'q': 'backurl=%2F'}

    with allure.step('Send request with data'):
        response = api_request(base_api_url, endpoint, 'POST', params=params)

    with allure.step('Checking status code'):
        assert response.status_code == 200
    with allure.step('Checking response'):
        assert response.json()['recaptcha']['isBot'] is False
        assert response.json()['hhcaptcha']['captchaError'] is None
    with allure.step('Checking validation'):
        validate(response.json(), load_json('correct_login.json'))


@allure.epic('Login')
@allure.story('Login user with incorrect data')
@allure.feature('Login')
@allure.tag('API')
@allure.label('owner')
@allure.severity('high')
def test_login_with_incorrect_data(base_api_url):
    endpoint = '/account/login'

    params = {'username': 'login', 'password': 'password', 'q': 'backurl=%2F'}

    with allure.step('Send request with incorrect data'):
        response = api_request(base_api_url, endpoint, 'POST', params=params)

    with allure.step('Checking status code'):
        assert response.status_code == 200
