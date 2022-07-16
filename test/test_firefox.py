import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_my_pets(driver_friends_firefox):
    driver_friends_firefox.implicitly_wait(10)
    driver_friends_firefox.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    driver_friends_firefox.implicitly_wait(10)
    assert driver_friends_firefox.find_element_by_xpath('//body/div[1]/div/div[1]/h2').text == "AnnaCherdan"
    driver_friends_firefox.close()
