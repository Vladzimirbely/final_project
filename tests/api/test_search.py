import allure
from jsonschema import validate
from rabotaby_project_tests.utils.load_json import load_json
from rabotaby_project_tests.utils.api_helper import api_request


@allure.epic('Search')
@allure.story('Search vacancies')
@allure.feature('Search')
@allure.tag('API')
@allure.label('owner')
@allure.severity('normal')
def test_search_vacancy(base_api_url):
    endpoint = '/vacancysuggest'
    data = {'q': 'PYTHON'}

    with allure.step('Send request'):
        response = api_request(base_api_url, endpoint, 'GET', params=data)

    with allure.step('Checking status code'):
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
def test_add_vacancy_to_favorite_without_registered(base_api_url):
    endpoint = '/applicant/favorite_vacancies/add'

    params = {'vacancyId': '100347198',
               'employerId': '5127780'}

    with allure.step('Send request'):
        response = api_request(base_api_url, endpoint, 'GET', params=params)

    with allure.step('Checking status code'):
        assert response.status_code == 404


@allure.epic('Otp')
@allure.story('Get Otp')
@allure.feature('Otp')
@allure.tag('API')
@allure.label('owner')
@allure.severity('normal')
def test_enter_phone_number_for_get_otp(base_api_url):
    num = '3752555555555'
    endpoint = '/account/otp_generate'

    params = {'login': num}

    with allure.step('Send request'):
        response = api_request(base_api_url, endpoint, 'POST', params=params)

    with allure.step('Checking status code'):
        assert response.status_code == 200
    with allure.step('Checking response'):
        assert response.json()['recaptcha']['isBot'] is False
        assert response.json()['recaptcha']['siteKey'] is not None
        assert response.json()['otp']['login'] == num
    with allure.step('Checking validation'):
        validate(response.json(), load_json('otp.json'))
