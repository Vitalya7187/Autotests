import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Base:
    """ Базовый класс, содержащий универсальные методы """


    def __init__(self, driver):
        self.driver = driver

    """"Возвращает текущую url страницы"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """"Перемещение к элементу на странице"""
    def move_to_element(self, element):
        self.element = element
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element).perform()
        print("Move to element")

    """"Перемещение и клик по элементу на странице"""
    def move_and_clik_to_element(self, element):
        self.element = element
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element).click().perform()
        print("Move and click to element")

    """"Сравнивает url на текущей странице с ожидаемым url"""
    def assert_url(self, result_url):
        current_url = self.driver.current_url
        assert current_url == result_url
        print("Get value url")

    """"Сравнивает текущую цену с ожидаемой ценой"""
    def assert_price(self, first_price, result_price_in_cart):
        assert first_price == result_price_in_cart
    #
    # def str_into_num(self, str):
    #     int_number = int(str)
    #     print(f"{int_number}")

    """"Получение текстового значения локатора"""
    def get_value_text(self, locator):
        self.locator = locator
        value_locator = locator.text
        print(f"{value_locator}")
        return value_locator

    """"Преобразование цены из текстового формата в числовой"""
    def item_price(self, locator_value):
        self.locator_value = locator_value
        symbols_to_remove = " ,₽"
        for symbol in symbols_to_remove:
            locator_value = locator_value.replace(symbol, "")
        return int(locator_value)
        # print(int(locator_value))

    """"Клик и удержание по элементу"""
    def clik_and_hold_to_element(self, element):
        self.element = element
        actions = ActionChains(self.driver)
        actions.click_and_hold(self.element).perform()
        print("Clik and hold to element")

    """"Перемещение к элементу в выпадающем списке"""
    def move_to_element_at_list(self, element):
        self.element = element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    """"Перемещение к раскрытому выпадающему списке"""
    def move_at_list(self, element):
        self.element = element
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        print("moving")


    def select_quantity(self, locator, quantity):
        i = 1
        self.locator = locator
        self.quantity = quantity
        while i != quantity:
            i+= 1
            locator.click()
            