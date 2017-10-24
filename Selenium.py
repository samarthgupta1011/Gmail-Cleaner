from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

a = raw_input("Enter number of mails to be deleted in multiple of 50 ")
a = int(a)
# For eg 250 is entered
a /= 50

email = raw_input("Enter your email ")
password = raw_input("Enter your password")

driver = webdriver.Chrome('/Users/samarthgupta/Downloads/chromedriver')
driver.get("https://mail.google.com/")
assert "Gmail" in driver.title

# Enter email
elem = driver.find_element_by_xpath('//*[@id="identifierId"]')
elem.clear()
elem.send_keys(email)

# Click next
elem = driver.find_element_by_xpath('//*[@id="identifierNext"]')
elem.send_keys(Keys.RETURN)

# Enter password
# Page takes time to load therefore using wait
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

elem = driver.find_element_by_name("password")
elem.send_keys(password)


# Click next
elem = driver.find_element_by_xpath('//*[@id="passwordNext"]')
elem.send_keys(Keys.RETURN)


# Page takes time to load therefore using wait
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id=":2p"]/div[5]'))
)

driver.find_element_by_xpath('//*[@id=":2p"]/div[5]').click()

for i in range(a):
    print (i)

    if i > 0:
        time.sleep(5)

    print("Wait over ie select all button visible ")
    driver.find_element_by_css_selector('div.T-Jo-auh').click()

    print("Wait over ie delete all button visible ")
    driver.find_element_by_css_selector('div.ar9.T-I-J3.J-J5-Ji').click()

assert "No results found." not in driver.page_source
driver.close()


