# import pytest
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# accept_button = "//div[@class='convergent-cookie-button']"
# def accept_button(self):
#     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_button)))
#
# @pytest.fixture(scope="module")
# def set_up():
#     accept_button().click()
#     yield