from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base
import time

"""Страница выбора конфигурации смартфона Huawei Nova 11"""
class NovaPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    black_nova_11 = "//div[@data-attrname='Черный']" # Черный цвет Huawei Nova 11
    yellow_huawei_band_9 = "//div[@colorname='Жёлтый']" # Желтый цвет Huawei band
    basket_button = "(//button[text()='В корзину'])[2]" # Кнопка корзины
    price_nova = "//p[@class='opt-price']" # Цена


    # Getters

    def get_black_nova_11(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.black_nova_11)))

    def get_yellow_huawei_band_9(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.yellow_huawei_band_9)))

    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))

    def get_price_nova(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.price_nova)))

    # Actions
    """Клик для выбора черного цвета Huawei Nova 11"""
    def click_black_nova_11(self):
        self.get_black_nova_11().click()

    """Клик для выбора синего цвета Huawei band 9"""
    def click_yellow_huawei_band_9(self):
        self.move_and_clik_to_element(self.get_yellow_huawei_band_9())

    """Перемещение и клик по кнопке корзины"""
    def move_and_click_to_basket_button(self):
        self.move_and_clik_to_element(self.get_basket_button())

    """Получение цены в текстовом формате"""
    def price_on_the_nova_11_page(self):
        return self.get_value_text(self.get_price_nova())


    # Methods
    """Выбор черного Huawei Nova 11 и синего Huawei band 9, получение цены в числовом формате и переход в корзину"""
    def select_black_nova_and_blue_band(self):
        self.click_black_nova_11()
        self.click_yellow_huawei_band_9()
        self.item_price(self.price_on_the_nova_11_page())
        self.move_and_click_to_basket_button()
        self.get_current_url()


