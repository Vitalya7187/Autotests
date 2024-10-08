import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base

"""Страница корзины"""
class CartPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    basket_button_cart_page = "//a[@cat='cart_cta_click']" # Кнопка купить
    title = "//h2[@class='login-title']" # Заголовок следующей страницы - Войти
    plus_button = "//button[@class='btn btn-light qty-add new-box']" # Кнопка плюс
    summary_price = "(//span[contains(@class, 'cart-list-price')])[5]" # Суммарная цена
    quantity_items_2 = "//input[@value='2']" # Количество отображаемых товаров

    # Getters

    def get_basket_button_cart_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button_cart_page)))

    def get_new_page(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.title)))

    def get_plus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_button)))

    def get_summary_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.summary_price)))

    def get_quantity_items_2(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.quantity_items_2)))

    # Actions

    """Нажатие по кнопке купить"""
    def click_basket_button_cart_page(self):
        self.get_basket_button_cart_page().click()

    """Клик по кнопке плюса 2 раза"""
    def click_plus_button(self):
        self.select_quantity(self.get_plus_button(),2)

    """Получение текстового значения цены"""
    def price_on_the_cart_page(self):
        return self.get_value_text(self.get_summary_price())

    """Выбор 2х товаров"""
    def price_2_items(self):
        return self.item_price(self.price_on_the_cart_page())

    # Methods
    """Нажатие по кнопке купить и ожидание появления заголовка следующей страницы - Войти"""
    def select_basket_button_cart_page(self):
        self.click_basket_button_cart_page()
        self.get_new_page()
        self.get_current_url()

    """Выбор 2х товаров"""
    def select_2_items_and_get_price(self):
        self.click_plus_button()
        self.get_quantity_items_2()
        self.price_2_items()
        print(self.price_2_items())
