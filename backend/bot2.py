from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://github.com/Alanzcc/selenium-bot")
driver.set_window_size(800, 600)
driver.find_element(
