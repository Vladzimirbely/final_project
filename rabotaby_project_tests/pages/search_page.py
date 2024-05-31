from selene import browser, have, command, be
import allure


class SearchPage:
    def open(self):
        with allure.step('Open browser'):
            browser.open('')
            return self

    def search_company(self):
        with allure.step('Enter word in input field'):
            browser.element('[data-qa="search-input"]').type('Yellow').press_enter()
        with allure.step('Close modal window'):
            browser.element('[data-qa="bloko-modal-close"]').click()
        with allure.step('Click on companies section'):
            browser.element('[data-hh-tab-id="employersList"]').click()
        with allure.step('Click on the "Yellow" company'):
            browser.element('.item--M8c5L2cxia1xqTMmWUFN .bloko-link.bloko-link_disable-visited').click()

    def should_have_company(self, data):
        browser.element('[data-qa="company-description-text"] .g-user-content').all('p').should(have.texts(
            data.main,
            data.goal,
            data.relationship,
            data.values,
            data.achievements,
            data.offer
        ))

    def search_with_filters(self, data):
        with allure.step('Click on filter button'):
            browser.element('[data-qa="advanced-search"]').click()
        with allure.step('Enter "Python" in keywords field'):
            browser.element('[data-qa="vacancysearch__keywords-input"]').type(data.python)
        with allure.step('Click on specialization section'):
            browser.element('[data-qa="bloko-suggest-list"] li:first-child').click()
        with allure.step('Choose specialization'):
            browser.element('[data-qa="resumesearch__profroles-switcher"]').click()
            browser.element(
                '[data-qa="bloko-tree-selector-item-text bloko-tree-selector-item-text-category-11"]').click()
            browser.element('[data-qa="bloko-tree-selector-popup-submit"]').click()
        with allure.step('Enter "3000" in income section'):
            browser.element('[data-qa="advanced-search-salary"]').type('3000')
        with allure.step('Enter submit button'):
            browser.element('[data-qa="advanced-search-submit-button"]').click()

    def should_have_search_with_filters(self, data):
        with allure.step('Checking input field'):
            browser.element('[data-qa="search-input"]').should(have.value(data.python))
        with allure.step('Checking header name of vacancy'):
            browser.element('[data-qa="bloko-header-3"]').should(have.text(data.python))

    def search_resume_page(self):
        with allure.step('Move to search resume section'):
            browser.element('[data-qa="remote-item-desktop"]').perform(command.js.scroll_into_view).click()
        with allure.step('Click on search resume button'):
            browser.element('[data-qa="bloko-modal-close"]').click()
        with allure.step('Click on resume section'):
            browser.element('[data-hh-tab-id="resumeSearch"]').click()
        with allure.step('Click on filter resume section'):
            browser.element('[data-qa="bloko-custom-select-select"]').click()

    def should_have_filter_section(self):
        with allure.step('Checking openning filters section'):
            browser.element('[data-qa="bloko-custom-select-option-list"]').should(be.visible)

    def save_search_without_registering(self):
        with allure.step('Enter word in input field'):
            browser.element('[data-qa="search-input"]').type('Python').press_enter()
        with allure.step('Close modal window'):
            browser.element('[data-qa="bloko-modal-close"]').click()
        with allure.step('Click on save search button'):
            browser.element('[data-qa="vacancy-saved-search-create"]').click()

    def should_have_text_registering(self):
        with allure.step('Checking moving to login page'):
            browser.element('[data-qa="account-postponed-vacancy-saved-search"]').should(have.text(
                'Войдите, чтобы сохранить поиск'
            ))

    def change_city(self):
        with allure.step('Click on location button'):
            browser.element('[data-qa="mainmenu_areaSwitcher"]').click()
        with allure.step('Choose Brest city'):
            browser.element('.area-switcher-cities li:nth-child(2) a').click()
        with allure.step('Click on filter button'):
            browser.element('[data-qa="advanced-search"]').click()
        with allure.step('Move to name of city'):
            browser.element('[data-qa="bloko-tag__text"]').perform(command.js.scroll_into_view).click()

    def should_be_city(self):
        with allure.step('Checking name of city in location'):
            browser.element('.supernova-navi-item_area-switcher-button').should(have.text('Брест'))
        with allure.step('Checking name of city in filters dection'):
            browser.element('[data-qa="bloko-tag__text"]').should(have.text('Брест'))


search_page = SearchPage()
