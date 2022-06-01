from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import motionarraygetlinks

#motionarraygetlinks.fetchlink()

list = []
tracker = 1

email = "Santilacazorla@gmail.com"
password = "t0075061h"

with open('templatelinks.txt') as npad:
    for line in npad:
        #print(line.strip(','))
        list.append(line)

### Set Options for Download Location ###

directory = "D:\PyCharm Projects\masspirate\Downloaded Items"

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", directory)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

browser = webdriver.Firefox(options=options)
browser.maximize_window()

for link in list:
    browser.get(link)

    if tracker == 1:
        login = browser.find_element(By.CSS_SELECTOR, 'a.flex:nth-child(2)')
        login.click()
        email_field = browser.find_element(By.CSS_SELECTOR, 'div.sm\:mt-8:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        email_field.send_keys(email)
        password_field = browser.find_element(By.CSS_SELECTOR, 'div.sm\:mt-8:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        password_field.send_keys(password)
        signin_button = browser.find_element(By.CSS_SELECTOR, 'button.w-full')
        signin_button.click()

    time.sleep(5)
    downloadbtn = browser.find_element(By.CSS_SELECTOR, 'button.flex-1')
    downloadbtn.click()

    time.sleep(5)
    tracker = tracker + 1


