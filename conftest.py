import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.set_headless(True)
    firefox_options.add_argument('--headless')
    return firefox_options


@pytest.fixture
def driver_friends(request):
    drifriend = webdriver.Firefox()
    drifriend.get('https://petfriends.skillfactory.ru/login')
    drifriend.find_element_by_xpath('//input[@id="email"]').send_keys('anchetest@mail.ru')
    drifriend.find_element_by_xpath('//*[@id="pass"]').send_keys('ljkmvtyf')
    drifriend.find_element_by_xpath('//body/div[1]/div[1]/form[1]/div[3]/button[1]').submit()
    return drifriend
