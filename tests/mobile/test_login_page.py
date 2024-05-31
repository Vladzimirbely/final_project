import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.epic('Login')
@allure.story('Login user with incorrect data')
@allure.feature('Login')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('high')
def test_login():
    with allure.step('Press login button'):
        browser.element((AppiumBy.ID,
                         'by.tut.jobs.android:id/fragment_intentions_onboarding_choose_direction_button_have_account')).click()

    with allure.step('Press login with password button'):
        browser.element((AppiumBy.XPATH,
                         '(//android.view.ViewGroup[@resource-id="by.tut.jobs.android:id/item_social_button_container"])[3]')).click()

    with allure.step('Checking input name'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Поиск работы"]')).should(have.text('Поиск работы'))
