from test_data.data import data_company, data_search_with_filter
from rabotaby_project_tests.pages.search_page import search_page
import allure
import pytest


@allure.epic('Search')
@allure.story('Search company')
@allure.feature('Search')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Search company')
def test_search_company():
    search_page.open()
    search_page.search_company()
    search_page.should_have_company(data_company)


@allure.epic('Search')
@allure.story('Search vacancies')
@allure.feature('Advanced search')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Advanced search')
def test_advanced_search():
    search_page.open()
    search_page.search_with_filters(data_search_with_filter)
    search_page.should_have_search_with_filters(data_search_with_filter)


@allure.epic('Resume')
@allure.story('Open resume')
@allure.feature('Resume')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Open resume page')
def test_open_resume_page():
    search_page.open()
    search_page.search_resume_page()
    search_page.should_have_filter_section()


@allure.epic('Search')
@allure.story('Search without registering')
@allure.feature('Search')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Save search without registering')
def test_save_search_without_registering():
    search_page.open()
    search_page.save_search_without_registering()
    search_page.should_have_text_registering()


@allure.epic('Choosing')
@allure.story('Choose company')
@allure.feature('Choosing')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
@pytest.mark.web
@pytest.mark.regress
@allure.title('Choose city')
def test_choose_city():
    search_page.open()
    search_page.change_city()
    search_page.should_be_city()
