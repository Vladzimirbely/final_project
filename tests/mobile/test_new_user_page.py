import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.epic('Registration')
@allure.story('Registration')
@allure.feature('Registration')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity('normal')
def test_registration_new_user():
    with allure.step('Press registration button'):
        browser.element((AppiumBy.ID,
                         'by.tut.jobs.android:id/fragment_intentions_onboarding_choose_direction_button_new_user')).click()

    with allure.step('Press registration with email or mobile button'):
        browser.element((AppiumBy.XPATH,
                         '(//android.view.ViewGroup[@resource-id="by.tut.jobs.android:id/item_social_button_container"])[3]')).click()

    with allure.step('Checking validation'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Электронная почта или телефон"]')).should(
            have.text('Электронная почта или телефон'))
        browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Быстрое создание резюме через соцсеть"]')).should(
            have.text('Быстрое создание резюме через соцсеть'))

    with allure.step('Press registration button without data'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Зарегистрироваться"]')).click()

    with allure.step('Checking validation of input'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Поле обязательно для заполнения"]')).should(
            have.text('Поле обязательно для заполнения'))
