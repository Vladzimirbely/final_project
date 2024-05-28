import os
import allure
from allure import attach
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from jsonschema import validate
from final_project.utils.load_json import load_json
import requests

page = 'https://rabota.by/'

@allure.epic('Login')
@allure.story('Login user with correct data')
@allure.feature('Login')
@allure.tag('API')
@allure.label('owner')
@allure.severity('high')
def test_login_with_correct_data():
    load_dotenv()

    login = os.getenv('user_login')
    password = os.getenv('user_password')
    url = 'account'
    data = 'login?backurl=%2F'

    payload = {'username': login,
               'password': password}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36'}

    with allure.step('Send request with data'):
        response = requests.post(f'{page}{url}/{data}', headers=headers, data=payload)
    cookies = response.cookies.get('_hi')
    with allure.step('Attach files'):
        attach(body=cookies, name='cookies', attachment_type=AttachmentType.TEXT)
    with allure.step('Checking status code'):
        assert response.status_code == 200
    with allure.step('Checking response'):
        assert response.json()['recaptcha']['isBot'] == False
        assert response.json()['hhcaptcha']['captchaError'] is None
    with allure.step('Checking validation'):
        validate(response.json(), load_json('correct_login.json'))

@allure.epic('Login')
@allure.story('Login user with incorrect data')
@allure.feature('Login')
@allure.tag('API')
@allure.label('owner')
@allure.severity('high')
def test_login_with_incorrect_data():
    url = 'account'
    data = 'login?backurl=%2F'

    payload = {'username': 'login',
               'password': 'password'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36'}
    with allure.step('Send request with incorrect data'):
        response = requests.post(f'{page}{url}/{data}', headers=headers, data=payload)
    cookies = response.cookies.get('hhtoken')
    with allure.step('Attach files'):
        attach(body=cookies, name='cookies', attachment_type=AttachmentType.TEXT)
    with allure.step('Checking status code'):
        assert response.status_code == 200
    with allure.step('Checking validation'):
        validate(response.json(), load_json('incorrect_login.json'))
