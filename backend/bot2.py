from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

USER = os.environ.get("USER_EMAIL")
PASSWORD = os.environ.get("USER_PASSWORD")
REPOSITORY = os.environ.get("REQUESTED_REPOSITORY")

driver.get(REPOSITORY)
driver.set_window_size(1920, 1080)
driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.implicitly_wait(5)

driver.find_element(By.ID, "login_field").click()
driver.find_element(By.ID, "login_field").send_keys(USER)
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "commit").click()
driver.implicitly_wait(5)

driver.find_element(By.ID, "issues-tab").click()

driver.find_element(By.LINK_TEXT, "New issue").click()
try:
	driver.find_element(By.ID, "issue_title").click()
except:
	driver.find_element(By.ID, "issue_title").click()
driver.find_element(By.ID, "issue_title").send_keys("Bot-issueing")
driver.find_element(By.ID, "issue_body").click()
driver.find_element(By.ID, "issue_body").send_keys("This issue was made by my selenium bot! I'm amazing")
driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/form/div/div/div[1]/div/div[1]/div/div[3]/button").click()

driver.quit()
