import pytest
from tests.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site/"

class TestLogin:
    def test_login_mail_button(driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys("olyaborovykh16123@ya.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION)).text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_account_button(driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys("olyaborovykh16123@ya.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION)).text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_registration_form(driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys("olyaborovykh16123@ya.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION)).text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_forgot_password_form(driver):
        driver.get(BASE_URL + "forgot-password")
        driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys("olyaborovykh16123@ya.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION)).text
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

class TestLogout:
    def test_logout(driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys("olyaborovykh16123@ya.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
