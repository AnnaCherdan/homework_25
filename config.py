# conftest
import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
# test_firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
link = 'https://petfriends.skillfactory.ru/login'
email = 'anchetest@mail.ru'
password = 'ljkmvtyf'
