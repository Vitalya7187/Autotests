import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base

"""Страница входа"""
class SignInPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    input_field = "//input[@type='text']" # Поле ввода почты
    check_box = "//p[text()='Я даю свое ']" # Чекбокс согласия
    continue_button = "//button[@id='login-continue']" # Кнопка продолжить


    # Getters

    def get_input_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_field)))

    def get_check_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    """Заполнение поля ввода почты"""
    def enter_input_field(self):
        self.get_input_field().send_keys("vit7@mail.ru")

    """Установка чекбокса"""
    def click_check_box(self):
        self.get_check_box().click()

    """Нажатие по кнопке продолжить"""
    def click_continue_button(self):
        self.get_continue_button().click()


    # Methods
    """Заполнение поля ввода почты, установка чекбокса и нажатие продолжить"""
    def input_email_and_click_continue(self):
        self.enter_input_field()
        self.click_check_box()
        self.click_continue_button()

