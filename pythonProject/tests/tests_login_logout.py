from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants


class TestLogin:
    def test_login_mail_button(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION)).text
        assert driver.current_url == Constants.BASE_URL

    def test_login_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION)).text
        assert driver.current_url == Constants.BASE_URL

    def test_login_registration_form(self, driver):
        driver.get(Constants.BASE_URL + "register")
        driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION)).text
        assert driver.current_url == Constants.BASE_URL

    def test_login_forgot_password_form(self, driver):
        driver.get(Constants.BASE_URL + "forgot-password")
        driver.find_element(*Locators.LOGIN_BUTTON_REG_FORM).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN_SECTION))
        assert driver.current_url == Constants.BASE_URL

class TestLogout:
    def test_logout(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
