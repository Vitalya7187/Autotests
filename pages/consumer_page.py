from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base

"""Страница потребителям"""
class ConsumerPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    smartphones = "(//a[@title='Смартфоны'])[1]" # Кнопка смартфоны
    accept_button_1 = "//div[@class='convergent-cookie-button']" # Кнопка принятия куки



    # Getters

    def get_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones)))

    def get_accept_button_1(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.accept_button_1)))

    # Actions

    """Клик по кнопке смартфоны"""
    def click_smartphones(self):
        self.get_smartphones().click()
        print("Click catalog menu")

    """Клик по кнопке принятия куки"""
    def select_accept_button_1(self):
        self.get_accept_button_1().click()
        print("Click catalog menu")


    # Methods
    """Клик по кнопке принятия куки и клик на кнопку смартфоны"""
    def select_smartphones(self):
        self.select_accept_button_1()
        self.click_smartphones()
        self.get_current_url()
        self.assert_url("https://consumer.huawei.com/ru/phones/")