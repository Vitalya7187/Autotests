from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base


"""Первая страница сайта Huawei"""
class FirstPage(Base):

    url = 'https://www.huawei.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators
    accept_button = "//button[@class='cookies-msg__close js-cookies-msg-close']" # Кнопка принятия куки
    consumer_button = "(//span[@class='header-nav__link'])[2]" # Кнопка для потребителей


    # Getters

    def get_consumer_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.consumer_button)))

    def get_accept_button(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.accept_button)))


    # Actions

    """Клик по кнопке для потребителей"""
    def select_consumer_button(self):
        self.get_consumer_button().click()
        print("Click consumer button")

    """Клик по кнопке принятия куки"""
    def select_accept_button(self):
        self.get_accept_button().click()
        print("Click catalog menu")


    # Methods
    """Открытие сайта Huawei, клик по кнопке принятия куки и клик на кнопку для потребителей"""
    def select_customer_page(self):
        self.driver.get(self.url)
        self.select_accept_button()
        self.select_consumer_button()
        self.get_current_url()
        self.assert_url("https://consumer.huawei.com/ru/")