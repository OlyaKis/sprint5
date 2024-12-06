import driver
import pytest
from tests.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site/"

class TestRegistration:
    def test_successful_registration(driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*Locators.NAME_INPUT).send_keys('Test test')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('olyaborovykh16157@ya.ru') # Генератор емейлов относится к доп. заданию, тут я использовала просто новый емейл
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        get_url = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.NAME_INPUT))
        assert get_url == BASE_URL

    def test_registration_with_short_password(driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*Locators.NAME_INPUT).send_keys('Test test')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('olyaborovykh16125@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        error_message = driver.find_element(*Locators.PASSWORD_ERROR).text
        assert error_message == "Некорректный пароль"
