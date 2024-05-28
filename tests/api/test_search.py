import allure
import requests
from allure import attach
from allure_commons.types import AttachmentType
from jsonschema import validate
from final_project.utils.load_json import load_json

page = 'https://rabota.by/'

@allure.epic('Login')
@allure.story('Login user with correct data')
@allure.feature('Login')
@allure.tag('API')
@allure.label('owner')
@allure.severity('normal')
def test_login_with_correct_data():
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

def test_add_vacancy_to_favorite_without_registered():
    url = 'applicant'
    data = 'favorite_vacancies/add'

    payload = {'vacancyId': '100347198',
               'employerId': '5127780'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
    }

    with allure.step('Send request'):
        response = requests.get(f'{page}{url}/{data}', headers=headers, data=payload)
    with allure.step('Checking status code'):
        assert response.status_code == 404
