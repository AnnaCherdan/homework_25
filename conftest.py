import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def set_headless(self, headless=True):
    # warnings.warn('use setter for headless property instead of set_headless',
    #               DeprecationWarning, stacklevel=2)
    self.headless = headless
    return headless


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless(True)
    chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture
def driver_friends_firefox(request):
    drifriend = webdriver.Firefox()
    drifriend.get('https://petfriends.skillfactory.ru/login')
    drifriend.find_element_by_xpath('//input[@id="email"]').send_keys('anchetest@mail.ru')
    drifriend.find_element_by_xpath('//*[@id="pass"]').send_keys('ljkmvtyf')
    drifriend.find_element_by_xpath('//body/div[1]/div[1]/form[1]/div[3]/button[1]').submit()
    return drifriend


@pytest.fixture
def driver_friends_chrome(request):
    drifriend = webdriver.Chrome()
    drifriend.get('https://petfriends.skillfactory.ru/login')
    drifriend.find_element_by_xpath('//input[@id="email"]').send_keys('anchetest@mail.ru')
    drifriend.find_element_by_xpath('//*[@id="pass"]').send_keys('ljkmvtyf')
    drifriend.find_element_by_xpath('//body/div[1]/div[1]/form[1]/div[3]/button[1]').submit()
    return drifriend