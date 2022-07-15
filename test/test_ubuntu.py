import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_my_pets(driver_friends):
    driver_friends.implicitly_wait(10)
    # time.sleep(5)
    driver_friends.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    driver_friends.implicitly_wait(10)
    # time.sleep(5)
    assert driver_friends.find_element_by_xpath('//body/div[1]/div/div[1]/h2').text == "AnnaCherdan"
    driver_friends.close()
