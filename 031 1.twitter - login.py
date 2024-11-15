from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize the Chrome driver with Service
website = "https://www.linkedin.com/login"
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(website)

username = driver.find_element(By.XPATH, '//input[@id="username"]')
password = driver.find_element(By.XPATH, '//input[@id="password"]')

username.send_keys('')
password.send_keys('')

login_button = driver.find_element(By.XPATH, '//button[@aria-label="Sign in"]')
login_button.click()
