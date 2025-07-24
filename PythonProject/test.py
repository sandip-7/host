import time
# from pynput.keyboard import Controller, Key
# from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from faker import Faker
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.common.alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome(service=Service('C:\\Users\\Dell\\PycharmProjects\\chromedriver.exe'))
driver.get('https://test.crm.infocarenepal.com/')
driver.maximize_window()
time.sleep(3)
try:
    # Wait and switch to alert
    alert = selenium.webdriver.common.alert.Alert(driver)
    alert.accept()  # Use accept() to accept the alert, or dismiss() to close it
except:
    print("No alert present")
    fake = Faker()

    # Generate fake data
    fake_name = fake.name()
    fake_email = fake.email()
    fake_address = fake.address()
    fake_Phone =fake.phone_number()

element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/input')
element.send_keys('sudoadmin@crm.com')

element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/input')
element.send_keys('Admin@123')
time.sleep(10)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/button[1]')
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/form/button')
element.click()
time.sleep(4)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[3]/ul/div[1]/ul/li[2]/div/a/span[2]')
element.click()
time.sleep(4)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div[1]/span')
element.click()
time.sleep(4)
name_field = driver.find_element(By.NAME, 'name')
name_field.send_keys(fake_name)
time.sleep(3)
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys(fake_email)
time.sleep(3)
phoneNumber_field = driver.find_element(By.NAME, 'phoneNumber')
phoneNumber_field.send_keys(fake_Phone)
time.sleep(3)
# dropdown = element.driver.find_element(By.CSS_SELECTOR, "select:nth-child(3)")
# dropdown.find_element(By.XPATH, "//option[. = 'DISTRIBUTOR']").click()
#
# # 21 | click | css=div:nth-child(1) > .pb-0
# element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .pb-0").click()
#
# time.sleep(5)
# select = Select(dropdown)


# element = driver.find_element(By.mro(), 'SUPPLIER')
# element.click()
# element.click()
# time.sleep(3)
# element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[1]/div[4]/div/select')  # Adjust the locator to match your form
# element.click()
# time.sleep(5)
# element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[1]/div[4]/div/select/option[2]')  # Adjust the locator to match your form
# element.click()
# time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[1]/select')  # Adjust the locator to match your form
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[1]/select/option[3]')  # Adjust the locator to match your form
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[2]/select')  # Adjust the locator to match your form
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[2]/select/option[4]')  # Adjust the locator to match your form
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[3]/select')  # Adjust the locator to match your form
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[3]/select/option[9]')  # Adjust the locator to match your form
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[4]/select/option[4]')  # Adjust the locator to match your form
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[3]/div/div[1]/div/input')  # Adjust the locator to match your form
element.send_keys('Admin@123')
element.click()
time.sleep(5)
email_field = driver.find_element(By.NAME, 'contactPersonEmail')
email_field.send_keys(fake_email)
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[3]/div/div[3]/div/input')  # Adjust the locator to match your form
element.send_keys('9876543210')
time.sleep(5)
address_field = driver.find_element(By.NAME, 'contactPersonAddress')
address_field.send_keys(fake_address)
time.sleep(3)
# element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[4]/select/option[4]')  # Adjust the locator to match your form
# element.click()
# time.sleep(5)
element= driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[4]/div/div[3]/div/input)
element.click()
time.sleep(3)
keyboard = Controller()
keyboard.type("C:\\Users\\Dell\\Downloads\\th.jfif")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[2]/button[2]')
element.click()
time.sleep(3)
