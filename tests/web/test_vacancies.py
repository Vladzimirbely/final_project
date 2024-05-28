from final_project.pages.data_company import DataCompany, DataSearchWithFilter
from final_project.pages.search_page import SearchPage
import allure

search_page = SearchPage()

@allure.epic('Search')
@allure.story('Search company')
@allure.feature('Search')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
def test_search_company():
    data = DataCompany(
        main = 'Yellow - молодая компания, которая занимается разработкой мобильных приложений, облачных систем, а также систем с использованием AI и машинного обучения',
        goal = 'Наш главный ориентир',
        relationship = 'Такого же отношения',
        values='Наши ценности',
        achievements = 'Наши достижения',
        offer = 'компания предлагает соискателям'
    )

    search_page.open()
    search_page.search_company()
    search_page.should_have_company(data)

@allure.epic('Search')
@allure.story('Search vacancies')
@allure.feature('Advanced search')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
def test_advanced_search():
    data = DataSearchWithFilter(
        python = 'Python'
    )

    search_page.open()
    search_page.search_with_filters(data)
    search_page.should_have_search_with_filters(data)

@allure.epic('Resume')
@allure.story('Open resume')
@allure.feature('Resume')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
def test_open_resume_page():
    search_page.open()
    search_page.search_resume_page()

@allure.epic('Search')
@allure.story('Search without registering')
@allure.feature('Search')
@allure.tag('web')
@allure.label('owner')
@allure.severity('normal')
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
def test_choose_city():
    search_page.open()
    search_page.change_city()
    search_page.should_be_city()
