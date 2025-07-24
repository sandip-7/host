import time
# from selenium.webdriver.chrome.options import Options
from faker import Faker
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome(service=Service('C:\\Users\\Dell\\PycharmProjects\\chromedriver.exe'))
driver.get('https://test.crm.infocarenepal.com/')
driver.maximize_window()
time.sleep(3)

# Handle possible alert
# try:
#     alert = driver.switch_to.alert
#     alert.accept()  # Use accept() to accept the alert, or dismiss() to close it
# except:
#     print("No alert present")

# Fake data generation
fake = Faker()
fake_name = fake.name()
fake_email = fake.email()
fake_address = fake.address()
fake_phone = fake.phone_number()

# Logging in
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/input').send_keys(
    'sudoadmin@crm.com')
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys(
    'Admin@123')
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/button[1]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/form/button').click()
time.sleep(4)

# Navigate through menus
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[3]/ul/div[1]/ul/li[2]/div/a/span[2]').click()
time.sleep(4)

# Click and fill out form
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div[1]/span').click()
time.sleep(4)

# Fill in the fields
driver.find_element(By.NAME, 'name').send_keys(fake_name)
time.sleep(3)
driver.find_element(By.NAME, 'email').send_keys(fake_email)
time.sleep(3)
driver.find_element(By.NAME, 'phoneNumber').send_keys("9801101234")
time.sleep(3)

# Dropdown selections (example, adjust as needed)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div['
                              '2]/div[2]/div/div[1]/select').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[1]/select/option[3]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[2]/select').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[2]/select/option[4]').click()
time.sleep(3)

# Contact details
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[3]/select').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[3]/select/option[9]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[4]/select').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/div/div[4]/select/option[4]').click()
time.sleep(3)
# Contact Person Details
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[3]/div/div[1]/div/input').send_keys(
    'Admin@123')
driver.find_element(By.NAME, 'contactPersonEmail').send_keys(fake_email)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[3]/div/div[3]/div/input').send_keys(
    '9876543210')
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[3]/div/div[4]/div/div/input').send_keys(
    'kathmandu')
time.sleep(3)

# File upload (corrected to use file input field directly)
element = driver.find_element(By.XPATH,
                              '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[1]/div[4]/div/div[3]/div/input')
element.send_keys("C:\\Users\\Dell\\Downloads\\th.jfif")
time.sleep(3)

# Submit form
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[2]/button[2]').click()
# Exit Button
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/form/div[2]/button[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[3]/ul/div[1]/ul/li[3]/div/a/span[2]').click()
time.sleep(3)
# # task planner
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[3]/ul/div[1]/ul/li[4]/div/a').click()
# time.sleep(5)
#
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span').click()
# time.sleep(3)
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div/input').send_keys("test")
# time.sleep(3)
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[2]/textarea').send_keys("test")
# time.sleep(3)
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[3]/div[1]/div/input').send_keys("122102025111111")
# time.sleep(3)
# element = driver.find_element(By.XPATH,
#                               '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[3]/div/div[3]/div/input')
# element.send_keys("C:\\Users\\Dell\\Downloads\\th.jfif")
# time.sleep(3)
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[2]/button[1]').click()
# time.sleep(5)
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[4]/td[8]/div/div[1]').click()
# time.sleep(3)
# driver.find_element(By.XPATH,
#                     '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div').click()
# time.sleep(3)