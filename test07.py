import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/hovers")
    time.sleep(1)

    not_checked1 = driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(3) > img:nth-child(1)")
    actions = ActionChains(driver)
    actions.move_to_Element(By.CSS_SELECTOR, "div.figure:nth-child(3) > img:nth-child(1)").perfoms()
    time.sleep(3)

finally:
    driver.quit()