import pytest
from tests.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_click_sauses(driver):
    driver.get(BASE_URL)
    driver.find_element(*Locators.SAUCE_SECTION).click()
    get_text = driver.find_element(*Locators.SAUCE_SECTION).text
    assert get_text == 'Соусы'
    driver.quit()

def test_click_fillings(driver):
    driver.get(BASE_URL)
    driver.find_element(*Locators.FILLING_SECTION).click()
    get_text = driver.find_element(*Locators.FILLING_SECTION).text
    assert get_text == 'Начинки'
    driver.quit()

def test_click_buns(driver):
    driver.get(BASE_URL)
    driver.find_element(*Locators.FILLING_SECTION).click()
    driver.find_element(*Locators.BUN_SECTION).click()
    get_text = driver.find_element(*Locators.BUN_SECTION).text
    assert get_text == 'Булки'
    driver.quit()