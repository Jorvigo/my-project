import time
#import win32api
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get('https://www3.animeflv.net/')
    time.sleep(5)
    link_serie = driver.find_element (By.CSS_SELECTOR, "#mCSB_1_container > ul > li:nth-child(1) > a")
    link_serie.click()
    link_episodio = driver.find_elements_by_css_selector, #episodeList > li:nth-child(2) > a > p
    assert link_episodio.text == 'Episodio 998'

    ##win32api.Message
finally:
    driver.quit()