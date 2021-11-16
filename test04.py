import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def comprar_billete(self):
        driver = webdriver.Chrome()
        driver.get("https://www.renfe.com/es/es")
        try
            

        self.assertEqual(driver.title, "Welcome to Python.org")  # add assertion here

