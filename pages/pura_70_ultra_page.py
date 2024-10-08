from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base
import time

"""Страница выбора конфигурации смартфона Huawei pura 70 ultra"""
class PuraPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    green_pura_70_ultra = "//div[@data-attrname='Зеленый']" # Зеленый цвет Huawei pura 70 ultra
    white_freeclip = "(//div[@class='bundle-sub-colorItem'])[2]" # белые наушники Huawei FreeClip
    basket_button = "//span[@class='btn-outer normal black hasborder smallCard summary-opt-btn opt-totalbtn-buynow']" # Кнопка корзины
    huawei_care = "(//div[@class='optser-seritem-liitem'])[2]" # Дополнительная гарантия
    price_pura_70_ultra = "//span[@class='total-price-sale']" # Цена


    # Getters

    def get_green_pura_70_ultra(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.green_pura_70_ultra)))

    def get_white_freeclip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.white_freeclip)))

    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))

    def get_huawei_care(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.huawei_care)))

    def get_price_pura_70_ultra(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_pura_70_ultra)))

    # Actions
    """ Перемещение и клик для выбора зеленого Huawei pura 70 ultra"""
    def click_green_pura_70_ultra(self):
        self.move_and_clik_to_element(self.get_green_pura_70_ultra())

    """Клик для выбора белого цвета Huawei FreeClip"""
    def click_white_freeclip(self):
        self.move_and_clik_to_element(self.get_white_freeclip())

    """Перемещение и клик по кнопке корзины"""
    def move_and_click_to_basket_button(self):
        self.move_and_clik_to_element(self.get_basket_button())

    """Перемещение и клик по кнопке дополнительной гарантии"""
    def move_and_click_to_huawei_care(self):
        self.move_and_clik_to_element(self.get_huawei_care())

    """Получение цены в текстовом формате"""
    def price_on_the_pura_70_ultra_page(self):
        return self.get_value_text(self.get_price_pura_70_ultra())


    # Methods
    """Выбор зеленого Huawei pura 70 ultra и белых Huawei FreeClip, получение цены в числовом формате и переход в корзину"""
    def select_green_pura_70_ultra_and_white_freeclip(self):
        self.click_green_pura_70_ultra()
        # self.click_white_freeclip()
        self.move_and_click_to_huawei_care()
        self.item_price(self.price_on_the_pura_70_ultra_page())
        self.move_and_click_to_basket_button()
        self.get_current_url()


