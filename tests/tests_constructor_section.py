import pytest
from tests.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site/"

class TestConstructorSection:
    def test_click_sauses(driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.SAUCE_SECTION).click()
        get_text = driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text
        assert get_text == 'Соусы'

    def test_click_fillings(driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.FILLING_SECTION).click()
        get_text = driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").text
        assert get_text == 'Начинки'

    def test_click_buns(driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.FILLING_SECTION).click()
        driver.find_element(*Locators.BUN_SECTION).click()
        get_text = driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text
        assert get_text == 'Булки'
