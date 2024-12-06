Этот проект предназначен для автоматизированного тестирования функциональности сайта Stellar Burgers. Автотесты написаны на Python с использованием библиотеки Selenium.

Тестируется:

tests_registration:
Успешная регистрация с корректными данными.
Проверка ошибки при регистрации с коротким паролем.

tests_login_logout:
Вход на сайт через кнопку «Войти в аккаунт».
Вход через кнопку «Личный кабинет».
Вход через форму регистрации.
Вход через форму восстановления пароля.
Выход из аккаунта. 

tests_click_on_account_and_constructor:
Переход в личный кабинет после авторизации.
Переход в конструктор после авторизации.

tests_constructor_section:
Переходы между разделами: «Булки», «Соусы», «Начинки».
