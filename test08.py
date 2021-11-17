import time

import driver as driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/windows")
    time.sleep(1)


    not_checked1 = driver.find_element(By.CSS_SELECTOR, ".example > a:nth-child(2)")
    not_checked1.click()

    driver.switch_to_window(driver.window_handles[1]

    text = driver.find_element(By.CSS_SELECTOR, ".example > h3:nth-child(1)")

    assert text.is_displayed()


    time.sleep(2)
finally:
    driver.quit()