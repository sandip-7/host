import time
# from selenium.webdriver.chrome.options import Options
# from faker import Faker
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
#
# Set up the WebDriver
driver = webdriver.Chrome(service=Service('C:\\Users\\Dell\\PycharmProjects\\chromedriver.exe'))
driver.get('https://hianimez.to/home')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="header_right"]/div/a').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(
    'sudoadmin@crm.com')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(
    'Admin@123')
time.sleep(5)