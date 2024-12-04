from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")     # Кнопка «Войти в аккаунт»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")      # Кнопка "Личный кабинет"
    LOGIN_BUTTON_REG_FORM = (By.XPATH, "//a[contains(text(),'Войти')]")     # Кнопка "Войти"
    LOGO = (By.CSS_SELECTOR, ".AppHeader_logo__link")       # Логотип Stellar Burgers
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")        # Кнопка "Конструктор"
    BUN_SECTION = (By.XPATH, "//span[text()='Булки']")      # Кнопка раздела "Булки"
    SAUCE_SECTION = (By.XPATH, "//h2[contains(text(),'Соусы')]")        # Кнопка раздела "Соусы"
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']")        # Кнопка раздела "Начинки"
    PASSWORD_INPUT = (By.NAME, "Пароль")        # Поле ввода пароля
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")      # Кнопка отправки формы входа
    NAME_INPUT = (By.NAME, "name")      # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")     # Поле ввода email
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")       # Кнопка регистрации
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")      # Сообщение об ошибке пароля
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")        # Кнопка выхода из аккаунта
