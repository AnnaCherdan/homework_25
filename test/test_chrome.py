import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_my_pets_info(driver_friends_chrome):
    driver_friends_chrome.implicitly_wait(10)
    driver_friends_chrome.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    driver_friends_chrome.implicitly_wait(10)
    assert driver_friends_chrome.find_element_by_xpath('//body/div[1]/div/div[1]/h2').text == "AnnaCherdan"
    driver_friends_chrome.implicitly_wait(10)
    pets = 'Питомцев: 5'
    pets_text = driver_friends_chrome.find_element_by_xpath('//body/div[1]/div[1]/div[1]')
    assert pets in pets_text.text
    string = driver_friends_chrome.find_elements_by_xpath('//table[@class ="table table-hover"]/tbody/tr')
    images = driver_friends_chrome.find_elements_by_css_selector('div#all_my_pets>table>tbody>tr>th>img')
    names = driver_friends_chrome.find_elements_by_xpath("//tr/td[1]")
    animal_type = driver_friends_chrome.find_elements_by_xpath('//tr/td[2]')
    age = driver_friends_chrome.find_elements_by_xpath('//tr/td[3]')
    driver_friends_chrome.implicitly_wait(10)
    assert names and animal_type and age != ''
    assert 'src' in images.text
    # for i in names:
    #     driver_friends_chrome.implicitly_wait(10)
    #     assert images[i].get_attribute('src') != ''
        # assert names[i].text != ''
    #     assert descriptions[i].text != ''
    #     assert ',' in descriptions[i]
    #     parts = descriptions[i].text.split(", ")
    #     assert len(parts[0]) > 0
    #     assert len(parts[1]) > 0

    driver_friends_chrome.close()


def test_all_pets_info(driver_friends_chrome):
    images = driver_friends_chrome.find_elements_by_css_selector('.card .card-img-top')
    names = driver_friends_chrome.find_elements_by_css_selector('.card-body .card-title')
    descriptions = driver_friends_chrome.find_elements_by_css_selector('.card-body .card-text')
    driver_friends_chrome.implicitly_wait(10)
    for i in range(len(names)):
        driver_friends_chrome.implicitly_wait(10)
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
