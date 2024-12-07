from locators import Locators


class TestConstructorSection:
    def test_click_sauses(self, driver):
        driver.find_element(*Locators.SAUCE_SECTION).click()
        get_text = driver.find_element(*Locators.H2_SAUCES).text
        assert get_text == 'Соусы'

    def test_click_fillings(self, driver):
        driver.find_element(*Locators.FILLING_SECTION).click()
        get_text = driver.find_element(*Locators.H2_FILLINGS).text
        assert get_text == 'Начинки'

    def test_click_buns(self, driver):
        driver.find_element(*Locators.FILLING_SECTION).click()
        driver.find_element(*Locators.BUN_SECTION).click()
        get_text = driver.find_element(*Locators.H2_BUNS).text
        assert get_text == 'Булки'
