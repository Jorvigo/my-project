import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(3)

    def marcar_add(add):

        not_checked1 = driver.find_element(By.CSS_SELECTOR, ".example > button:nth-child(1)")
        not_checked1.click()
        delete = int (driver.find_element(By.CSS_SELECTOR, "button.added-manually:nth-child(1)"))
        if delete <= 10:
            not_checked1.click()

finally:
    driver.quit()