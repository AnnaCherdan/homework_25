import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless(True)
    chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture
def driver_friends_chrome(request):
    drifriend = webdriver.Chrome()
    drifriend.get('https://petfriends.skillfactory.ru/login')
    drifriend.find_element_by_xpath('//input[@id="email"]').send_keys('anchetest@mail.ru')
    drifriend.find_element_by_xpath('//*[@id="pass"]').send_keys('ljkmvtyf')
    drifriend.find_element_by_xpath('//body/div[1]/div[1]/form[1]/div[3]/button[1]').submit()
    return drifriend