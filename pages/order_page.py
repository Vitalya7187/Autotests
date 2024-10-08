import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base

"""Страница оформления заказа"""
class OrderPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    name_field = "(//input[@name='consignee'])[1]" # Поле ввода имени
    phone_field = "(//input[@name='mobile'])[1]" # Поле ввода номера
    province_field = "(//input[@name='provinceName'])[1]" # Поле ввода региона
    province_list = "(//ul[@class='swiper-slide addr_province_list'])[1]" # Выпадающий список регионов
    khakassia_field = "//li[@title='Хакасия респ.']" # Пункт выпадающего списка - Хакасия респ.
    abakan_field_city = "//li[@title='Абакан']" # Пункт выпадающего списка - город Абакан
    city_field = "(//input[@name='cityName'])[1]" # Поле ввода города
    city_list = "//div[@class='dropdown-menu scroll-content ps show']" # Выпадающий список городов
    zip_code_field = "(//input[@name='zipCode'])[1]" # Поле ввода индекса
    street_field = "(//input[@name='aliasStreetName'])[1]" # Поле ввода улицы
    adress_field = "(//input[@name='address'])[1]" # Поле ввода дома
    apartment_field = "(//input[@name='building'])[1]" # Поле ввода квартиры



    # Getters

    def get_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_province_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.province_field)))

    def get_province_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.province_list)))

    def get_scroll(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.scroll)))

    def get_khakassia_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.khakassia_field)))

    def get_city_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_field)))

    def get_city_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_list)))

    def get_abakan_field_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.abakan_field_city)))

    def get_zip_code_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code_field)))

    def get_street_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_field)))

    def get_adress_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_field)))

    def get_apartment_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apartment_field)))


    # Actions

    """Заполнение поле имя"""
    def enter_name_field(self):
        self.get_name_field().send_keys("John")

    """Заполнение поле телефона"""
    def enter_phone_field(self):
        self.get_phone_field().send_keys("9885346798")

    """Клик по полю региона"""
    def click_province_field(self):
        self.get_province_field().click()

    """Перемещение к раскрытому выпадающему списку регионов"""
    def move_to_province_list(self):
        self.move_to_element(self.get_province_list())

    """Заполнение поля региона"""
    def enter_province_field(self):
        self.get_province_field().send_keys("Хакасия респ.")

    """Клик и перемещение к региону Хакасия"""
    def click_khakassia_field(self):
        self.move_and_clik_to_element(self.get_khakassia_field())

    """Клик по полю города"""
    def click_city_field(self):
        self.get_city_field().click()

    """Заполнение поля города"""
    def enter_city_field(self):
        self.get_city_field().send_keys("Абакан")

    """Перемещение к раскрытому выпадающему списку городов"""
    def move_to_city_list(self):
        self.move_to_element(self.get_city_list())

    """Клик и перемещение к городу Абакан"""
    def click_abakan_field_city(self):
        self.move_and_clik_to_element(self.get_abakan_field_city())

    """Заполнение поля индекса"""
    def enter_zip_code_field(self):
        self.get_zip_code_field().send_keys("101002")

    """Заполнение поля улицы"""
    def enter_street_field(self):
        self.get_street_field().send_keys("Тверская")

    """Заполнение поля дома"""
    def enter_adress_field(self):
        self.get_adress_field().send_keys("4")

    """Заполнение поля квартиры"""
    def enter_apartment_field(self):
        self.get_apartment_field().send_keys("44")


    # Methods

    """Заполнение всех полей на странице заказа"""
    def enter_all_order_fields(self):
        self.enter_name_field()
        self.enter_phone_field()
        self.click_province_field()
        self.enter_province_field()
        self.move_to_province_list()
        self.click_khakassia_field()
        self.click_city_field()
        self.enter_city_field()
        self.move_to_city_list()
        self.click_abakan_field_city()
        self.enter_zip_code_field()
        self.enter_street_field()
        self.enter_adress_field()
        self.enter_apartment_field()
        self.get_current_url()

