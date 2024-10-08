import time

from selenium import webdriver

from pages.cart_page import CartPage
from pages.consumer_page import ConsumerPage
from pages.first_page import FirstPage
from pages.about_nova_11_page import AboutNovaPage
from pages.nova_11_page import NovaPage
from pages.pura_70_ultra_page import PuraPage
from pages.smartphones_page import SmartphonesPage


def test_1_compare_price_2_huawei_nova_11():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Start Test 1")

    main = FirstPage(driver)
    main.select_customer_page()
    consumer = ConsumerPage(driver)
    consumer.select_smartphones()
    huawei_nova_11 = SmartphonesPage(driver)
    huawei_nova_11.select_huawei_nova_11()
    nova_11 = AboutNovaPage(driver)
    nova_11.select_buy_button()
    black_nova_11_and_blue_band = NovaPage(driver)
    black_nova_11_and_blue_band.select_black_nova_and_blue_band()
    cart_1 = CartPage(driver)
    cart_1.select_2_items_and_get_price()
    assert cart_1.price_2_items() == 55998

def test_2_compare_price_2_huawei_pura_70_ultra():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Start Test 2")

    main = FirstPage(driver)
    main.select_customer_page()
    consumer_2 = ConsumerPage(driver)
    consumer_2.select_smartphones()
    smartphones_pura_70_ultra = SmartphonesPage(driver)
    smartphones_pura_70_ultra.select_pura_70_ultra()
    huawei_pura_70_ultra = PuraPage(driver)
    huawei_pura_70_ultra.select_green_pura_70_ultra_and_white_freeclip()
    cart_2 = CartPage(driver)
    cart_2.select_2_items_and_get_price()
    assert cart_2.price_2_items() == 237978



