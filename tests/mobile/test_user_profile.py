import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.epic('Vacancy page')
@allure.story('Vacancy')
@allure.feature('Vacancy page')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('normal')
def test_registration_new_user():
    with allure.step('Close window'):
        browser.element(
            (AppiumBy.ID, 'by.tut.jobs.android:id/fragment_intentions_onboarding_choose_direction_image_close')).click()

    with allure.step('Open profile'):
        browser.element((AppiumBy.XPATH,
                         '(//android.widget.ImageView[@resource-id="by.tut.jobs.android:id/bottom_navigation_item_icon"])[5]')).click()

    with allure.step('Checking text'):
        browser.element((AppiumBy.ID, 'by.tut.jobs.android:id/view_error_text_title')).should(
            have.text('Создать резюме'))
