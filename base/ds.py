import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "https://klik-test.ru/schetchik-klikov"
driver.get(url)

element_1 = driver.find_element(By.XPATH, "//button[@id='click-plus']")

def clicker(element_1,number=0):
    i = 0
    while i != number:
        i+=1
        element_1.click()

clicker(element_1, 500)
time.sleep(5)
