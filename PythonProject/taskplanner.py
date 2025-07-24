import time
# from selenium.webdriver.chrome.options import Options
# from faker import Faker
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome(service=Service('C:\\Users\\Dell\\PycharmProjects\\chromedriver.exe'))
driver.get('https://test.crm.infocarenepal.com/')
driver.maximize_window()
time.sleep(3)
try:
    alert = driver.switch_to.alert
    alert.accept()  # Use accept() to accept the alert, or dismiss() to close it
except:
    print("No alert present")
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
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[3]/ul/div[1]/ul/li[4]/div/a').click()
time.sleep(5)

driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div/input').send_keys("test")
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[2]/textarea').send_keys("test")
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[3]/div[1]/div/input').send_keys("111100202511111")
time.sleep(3)
element = driver.find_element(By.XPATH,
                              '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[3]/div/div[3]/div/input')
element.send_keys("C:\\Users\\Dell\\Downloads\\th.jfif")
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[2]/button[2]').click()
time.sleep(5)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[4]/td[8]/div/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[4]/td[8]/div/div[2]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[2]/button[2]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/table/tbody/tr[4]/td[8]/div/div[3]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/form/div[2]/button[2]').click()
time.sleep(3)
driver.find_element(By.XPATH,
                    '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[3]/ul/div[1]/ul/li[5]/div/a/span[2]').click()
time.sleep(3)
