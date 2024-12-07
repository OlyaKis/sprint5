from tests.locators import Locators
from constants import Constants


class TestClickOnAccountButton:
    def test_click_account_page(self, driver):
        driver.get(Constants.BASE_URL)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == Constants.BASE_URL + 'account'

class TestClickFromAccountToConstructor:
    def test_click_constructor_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.current_url == Constants.BASE_URL
