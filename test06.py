import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(1)

    not_checked1 = driver.find_element(By.CSS_SELECTOR, ".example > ul:nth-child(3) > li:nth-child(1) > button:nth-child(1)")
    not_checked1.click()
    time.sleep(2)

    alerta = "I am a JS Alert"
    from selenium.webdriver.common.action_chains import ActionChains

    while not alerta.isdisplayed():
        actions.send_keys(Keys.RETURN)

        actions.perform()
        sehahechoclick = driver.find_element(By.CSS_SELECTOR, "#result")
    assert sehahechoclick.text == "You successfully clicked an alert"


finally:
    driver.quit()
