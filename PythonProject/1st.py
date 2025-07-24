from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
# import selenium.webdriver.common.alert
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from test import element
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(service=Service('C:\\Users\\Dell\\PycharmProjects\\chromedriver.exe'))
driver.get('https://test.crm.infocarenepal.com/')
driver.maximize_window()
time.sleep(3)
element.driver.find_element(By.NAME, "email").send_keys("sudoadmin@crm.com")
        # 4 | type | name=password | Admin@123
# 1 | type | name=password | Admin@123
element.driver.find_element(By.NAME, "password").send_keys("Admin@123")

# 2 | click | name=email
element.driver.find_element(By.NAME, "email").click()

# 3 | click | css=.hover\3A bg-slate-50
element.driver.find_element(By.CSS_SELECTOR, ".hover\\3A bg-slate-50").click()
time.sleep(9)
# 4 | click | css=.mb-4:nth-child(2) path:nth-child(4)
element.driver.find_element(By.CSS_SELECTOR, ".mb-4:nth-child(2) path:nth-child(4)").click()

# 5 | click | css=.whitespace-nowrap
element.driver.find_element(By.CSS_SELECTOR, ".whitespace-nowrap").click()

# 6 | click | css=ul:nth-child(1) > .text-accent-foreground:nth-child(2) .mb-\[-2px\]
element.driver.find_element(By.CSS_SELECTOR,
                            "ul:nth-child(1) > .text-accent-foreground:nth-child(2) .mb-\\[-2px\\]").click()

# 7 | click | css=.bg-primary > .md\3A flex
element.driver.find_element(By.CSS_SELECTOR, ".bg-primary > .md\\3A flex").click()

# 8 | click | name=name
element.driver.find_element(By.NAME, "name").click()

# 9 | type | name=name | sasda
element.driver.find_element(By.NAME, "name").send_keys("sasda")

# 10 | click | name=email
element.driver.find_element(By.NAME, "email").click()

# 11 | type | name=email | sasasa@gmail.com
element.driver.find_element(By.NAME, "email").send_keys("sasasa@gmail.com")

# 12 | click | name=phoneNumber
element.driver.find_element(By.NAME, "phoneNumber").click()

# 13 | click | name=phoneNumber
element.driver.find_element(By.NAME, "phoneNumber").click()

# 14 | doubleClick | name=phoneNumber
element = element.driver.find_element(By.NAME, "phoneNumber")
actions = ActionChains(element.driver)
actions.double_click(element).perform()
# 15 | type | name=phoneNumber | 98442251362
element.driver.find_element(By.NAME, "phoneNumber").send_keys("98442251362")

# 16 | click | css=.pb-4
element.driver.find_element(By.CSS_SELECTOR, ".pb-4").click()

# 17 | mouseOver | css=div:nth-child(1) > .text-\[13px\]
element = element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .text-\\[13px\\]")
actions = ActionChains(element.driver)
actions.move_to_element(element).perform()

# 18 | mouseOut | css=div:nth-child(1) > .text-\[13px\]
element = element.driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(element.driver)
# actions.move_to_element(element, 0, 0).perform()

# 19 | click | css=html
element.driver.find_element(By.CSS_SELECTOR, "html").click()

# 20 | select | css=select:nth-child(3) | label=DISTRIBUTOR
dropdown = element.driver.find_element(By.CSS_SELECTOR, "select:nth-child(3)")
dropdown.find_element(By.XPATH, "//option[. = 'DISTRIBUTOR']").click()

# 21 | click | css=div:nth-child(1) > .pb-0
element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .pb-0").click()

# 22 | select | css=.border-gray | label=Madhesh Pradesh
dropdown = element.driver.find_element(By.CSS_SELECTOR, ".border-gray")
dropdown.find_element(By.XPATH, "//option[. = 'Madhesh Pradesh']").click()

# 23 | click | css=div:nth-child(2) > .pb-0
element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pb-0").click()

# 24 | select | css=div:nth-child(2) > .pb-0 | label=Siraha
dropdown = element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pb-0")
dropdown.find_element(By.XPATH, "//option[. = 'Siraha']").click()

# 25 | click | css=div:nth-child(3) > .pb-0
element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .pb-0").click()

# 26 | select | css=div:nth-child(3) > .pb-0 | label=Lahan Municipality
dropdown = element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .pb-0")
dropdown.find_element(By.XPATH, "//option[. = 'Lahan Municipality']").click()

# 27 | click | css=.border-red-500
element.driver.find_element(By.CSS_SELECTOR, ".border-red-500").click()

# 28 | select | css=div:nth-child(4) > .pb-0 | label=3
dropdown = element.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > .pb-0")
dropdown.find_element(By.XPATH, "//option[. = '3']").click()

# 29 | click | name=contactPersonName
element.driver.find_element(By.NAME, "contactPersonName").click()

# 30 | type | name=contactPersonName | Bijaya Shah
element.driver.find_element(By.NAME, "contactPersonName").send_keys("Bijaya Shah")

# 31 | type | name=contactPersonName | Bijaya Shahwq
element.driver.find_element(By.NAME, "contactPersonName").send_keys("Bijaya Shahwq")
