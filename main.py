# References
# - https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
# - https://stackoverflow.com/questions/75652543/clicking-the-button-with-selenium-python
# - https://www.pythonanywhere.com/pricing/

import os
import logging

from dotenv import load_dotenv, find_dotenv
# Using Selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv(find_dotenv())
logging.basicConfig(format='%(asctime)s - %(message)s', level=int(os.environ.get("LOGGING", 20)))

# browserless.io configuration
token = os.environ.get("TOKEN")
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserless:token', token)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor='https://chrome.browserless.io/webdriver',
    options=chrome_options
)

target_domain = "https://stackoverflow.com/users/login?ssrc=head"
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

driver.get(target_domain)
logging.info(driver.title)

# find username/email field and send the username itself to the input field
driver.find_element(By.ID, "email").send_keys(email)
# find password input field and insert password as well
driver.find_element(By.ID, "password").send_keys(password)

# try to accept cookies if needed
driver.maximize_window()
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.js-reject-cookies"))).click()
    logging.info("Cookies rejected...")
except:
    logging.info("Proceeding with login...")

# click login button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "submit-button"))).click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "The email or password is incorrect."
# get the errors (if any)
errors = driver.find_elements("css selector", ".has-error")
# print the errors optionally
# for e in errors:
#     logging.error(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    logging.error("[!] Login failed")
else:
    logging.info("[+] Login successful")

# go to profile and get the +1 for consecutive day!
driver.find_element(By.CSS_SELECTOR, "img.js-avatar-me").click()
#logging.info(driver.find_element(By.CSS_SELECTOR, "div.fs-title").text)

driver.quit()
