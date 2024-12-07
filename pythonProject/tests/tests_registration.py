from tests.locators import Locators
from constants import Constants
from faker import Faker
import time


faker = Faker()

class TestRegistration:
    def test_successful_registration(self, driver):
        email = faker.email()
        driver.get(Constants.BASE_URL + "register")
        driver.find_element(*Locators.NAME_INPUT).send_keys('Test test')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        time.sleep(3)
        assert driver.current_url == Constants.BASE_URL + "login"

    def test_registration_with_short_password(self, driver):
        email = faker.email()
        driver.get(Constants.BASE_URL + "register")
        driver.find_element(*Locators.NAME_INPUT).send_keys('Test test')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        error_message = driver.find_element(*Locators.PASSWORD_ERROR).text
        assert error_message == "Некорректный пароль"
