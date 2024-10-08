from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base

"""Страница Nova 11"""
class AboutNovaPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    buy_button = "//button[@title='Купить']" # Кнопка купить


    # Getters

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    # Actions

    """Клик по кнопке купить"""
    def click_buy_button(self):
        self.get_buy_button().click()


    # Methods

    """Клик по кнопке купить"""
    def select_buy_button(self):
        self.click_buy_button()
        self.get_current_url()
        self.assert_url("https://consumer.huawei.com/ru/phones/nova11/buy/")
