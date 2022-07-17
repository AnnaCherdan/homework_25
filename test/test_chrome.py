import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_my_pets_info(driver_friends_chrome):
    driver_friends_chrome.implicitly_wait(10)
    driver_friends_chrome.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    assert driver_friends_chrome.find_element_by_xpath('//body/div[1]/div/div[1]/h2').text == "AnnaCherdan"

    pets = 'Питомцев: 5'
    pets_text = driver_friends_chrome.find_element_by_xpath('//body/div[1]/div[1]/div[1]')
    assert pets in pets_text.text

    string = driver_friends_chrome.find_elements_by_xpath('//table[@class ="table table-hover"]/tbody/tr')

    images = driver_friends_chrome.find_elements_by_css_selector('div#all_my_pets>table>tbody>tr>th>img')
    names = driver_friends_chrome.find_elements_by_xpath("//tr/td[1]")
    animal_type = driver_friends_chrome.find_elements_by_xpath('//tr/td[2]')
    age = driver_friends_chrome.find_elements_by_xpath('//tr/td[3]')
    table_pet = driver_friends_chrome.find_elements_by_xpath('//*[@id="all_my_pets"]/table')
    for i in range(len(string)):
        assert names[i].text and animal_type[i].text and age[i].text != ''
        # assert images[i].get_attribute('src') != '', 'WARNING, no IMG'
        count_img = img
        if images[i].get_attribute('src') != '':
            img = len(images)
        count_img = img
        count_nam = len(names)
        assert img == count_nam








    # for string in range(len(table_pet)):
    #     assert string == images




    # table_pet = driver_friends_chrome.find_elements_by_xpath('//*[@id="all_my_pets"]/table')
    # for i in range(len(table_pet)):
    #
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
