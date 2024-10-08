from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base

"""Страница смартфонов Huawei"""
class SmartphonesPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    nova_11 = "//li[@class='product-item product-card product-card-item swiper-slide swiper-slide-active']" # HUAWEI nova 11
    pura_70_ultra = "(//a[@href='/ru/phones/pura70-ultra/'])[5]" # HUAWEI pura 70 ultra

    # Getters

    def get_nova_11(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nova_11)))

    def get_pura_70_ultra(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pura_70_ultra)))

    # Actions
    """Перемещение и клик по HUAWEI nova 11"""
    def move_to_nova_11(self):
        self.move_and_clik_to_element(self.get_nova_11())

    """Перемещение и клик по HUAWEI pura 70 ultra"""
    def move_to_pura_70_ultra(self):
        self.move_and_clik_to_element(self.get_pura_70_ultra())

    # Methods
    """Перемещение и клик по HUAWEI nova 11"""
    def select_huawei_nova_11(self):
        self.move_to_nova_11()
        self.get_current_url()
        self.assert_url("https://consumer.huawei.com/ru/phones/nova11/")

    """Перемещение и клик по HUAWEI pura 70 ultra"""
    def select_pura_70_ultra(self):
        self.move_to_pura_70_ultra()
        self.get_current_url()
        self.assert_url("https://consumer.huawei.com/ru/offer/smartphones/pura-70-ultra-buy/")