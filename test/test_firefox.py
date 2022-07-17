import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_my_pets(driver_friends_firefox):
    driver_friends_firefox.implicitly_wait(10)
    driver_friends_firefox.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    driver_friends_firefox.implicitly_wait(10)
    assert driver_friends_firefox.find_element_by_xpath('//body/div[1]/div/div[1]/h2').text == "AnnaCherdan"
    driver_friends_firefox.implicitly_wait(10)
    pets = 'Питомцев: 5'
    pets_text = driver_friends_firefox.find_element_by_xpath('//body/div[1]/div[1]/div[1]')
    assert pets in pets_text.text
    string = driver_friends_firefox.find_elements_by_xpath('//table[@class ="table table-hover"]/tbody/tr')
    images = driver_friends_firefox.find_elements_by_css_selector('div#all_my_pets>table>tbody>tr>th>img')
    names = driver_friends_firefox.find_elements_by_xpath("//tr/td[1]")
    animal_type = driver_friends_firefox.find_elements_by_xpath('//tr/td[2]')
    age = driver_friends_firefox.find_elements_by_xpath('//tr/td[3]')
    driver_friends_firefox.implicitly_wait(10)
    # assert names and animal_type and age != ''
    for i in string:
        assert names[i] and animal_type[i] and age[i] != ''
    driver_friends_firefox.close()
