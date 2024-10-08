from selenium import webdriver

from pages.cart_page import CartPage
from pages.consumer_page import ConsumerPage
from pages.first_page import FirstPage
from pages.about_nova_11_page import AboutNovaPage
from pages.nova_11_page import NovaPage
from pages.order_page import OrderPage
from pages.pura_70_ultra_page import PuraPage
from pages.sign_in_page import SignInPage
from pages.smartphones_page import SmartphonesPage
import time

def test_1_buy_huawei_nova_11():
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
    cart_1.select_basket_button_cart_page()
    sign_in = SignInPage(driver)
    sign_in.input_email_and_click_continue()
    confirm_order = OrderPage(driver)
    confirm_order.enter_all_order_fields()


def test_2_buy_huawei_pura_70_ultra():
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
    cart_2.select_basket_button_cart_page()
    sign_in_2 = SignInPage(driver)
    sign_in_2.input_email_and_click_continue()
    confirm_order_2 = OrderPage(driver)
    confirm_order_2.enter_all_order_fields()
