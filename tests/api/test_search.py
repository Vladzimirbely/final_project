import allure
import requests
from allure import attach
from allure_commons.types import AttachmentType
from jsonschema import validate
from rabotaby_project_tests.utils.load_json import load_json

page = 'https://rabota.by/'


@allure.epic('Search')
@allure.story('Search vacancies')
@allure.feature('Search')
@allure.tag('API')
@allure.label('owner')
@allure.severity('normal')
def test_search_vacancy():
    url = 'vacancysuggest'
    data = '?q=PYTHON'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36'}

    with allure.step('Send request'):
        response = requests.get(f'{page}{url}/{data}', headers=headers)
    with allure.step('Checking status code'):
        print(response.content)
        assert response.status_code == 200
    with allure.step('Checking response'):
        assert response.json()['items'] is not None
    with allure.step('Checking validation'):
        validate(response.json(), load_json('search_vacancies.json'))


@allure.epic('Search')
@allure.story('Add vacancy to favorite')
@allure.feature('Search')
@allure.tag('API')
@allure.label('owner')
@allure.severity('normal')
def test_add_vacancy_to_favorite_without_registered():
    url = 'applicant'
    data = 'favorite_vacancies/add'

    payload = {'vacancyId': '100347198',
               'employerId': '5127780'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36'
    }

    with allure.step('Send request'):
        response = requests.get(f'{page}{url}/{data}', headers=headers, data=payload)
    with allure.step('Checking status code'):
        assert response.status_code == 404


@allure.epic('Otp')
@allure.story('Get Otp')
@allure.feature('Otp')
@allure.tag('API')
@allure.label('owner')
@allure.severity('normal')
def test_enter_phone_number_for_get_otp():
    url = 'account'
    data = 'otp_generate'
    num = '3752555555555'

    payload = {'login': num}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36'
    }

    with allure.step('Send request'):
        response = requests.post(f'{page}{url}/{data}', headers=headers, data=payload)
    json = response.text
    with allure.step('Attach files'):
        attach(body=json, name='json', attachment_type=AttachmentType.TEXT)
    with allure.step('Checking status code'):
        assert response.status_code == 200
    with allure.step('Checking response'):
        assert response.json()['recaptcha']['isBot'] == False
        assert response.json()['recaptcha']['siteKey'] is not None
        assert response.json()['otp']['login'] == num
    with allure.step('Checking validation'):
        validate(response.json(), load_json('otp.json'))
