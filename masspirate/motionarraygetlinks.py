from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def fetchlink():
    with open('templatelinks.txt', 'w') as notepad:

        email = "Santilacazorla@gmail.com"
        password = "t0075061h"

        browser = webdriver.Firefox()
        browser.maximize_window()

        startlink = "https://motionarray.com"
        browser.get(startlink)
        time.sleep(1)
        login = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div[1]/div[3]/a[2]')
        login.click()
        email_field = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/div[2]/div/form/div[1]/div/div[1]/input')
        email_field.send_keys(email)
        password_field = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/div[2]/div/form/div[2]/div/div[1]/input')
        password_field.send_keys(password)
        signin_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div/div[2]/div/form/div[4]/button')
        signin_button.click()
        time.sleep(1)

        print("----- Select Adobe Type: (This line of codes only work for the template options) -----")
        print("1: Adobe After Effects")
        print("2: Adobe Premiere Pro")
        print("3: Motion Graphics")
        print("4: Adobe Premiere Rush")
        print("5: DaVinci Resolve")
        print("6: Final Cut Pro")
        adobeselect = int(input("Select Option 1 to 6 (Only Option 1 works in this version): "))

        if adobeselect == 1:
            midlink1 = "/browse/after-effects-templates"
        if adobeselect == 2:
            midlink1 = "/browse/premiere-pro-templates"
        if adobeselect == 3:
            midlink1 = "/browse/motion-graphics-templates"
        if adobeselect == 4:
            midlink1 = "/browse/premiere-rush-templates"
        if adobeselect == 5:
            midlink1 = "/browse/davinci-resolve-templates"
        if adobeselect == 6:
            midlink1 = "/browse/final-cut-pro-templates"

        print("----- Select Subcategory: (This line of codes only work for the template options) -----")
        print("1: Photo /Video")
        print("2: Text")
        print("3: Logo")
        print("4: Lower Thirds")
        print("5: Transitions")
        print("6: Other")
        print("7: Slideshows")
        print("8: Intros")
        subcatselect = int(input("Select Option 1 to 8: "))

        if subcatselect == 1:
            subcatoption = "photo-video-1"
        if subcatselect == 2:
            subcatoption = "text-2"
        if subcatselect == 3:
            subcatoption = "logos"
        if subcatselect == 4:
            subcatoption = "lower-thirds"
        if subcatselect == 5:
            subcatoption = "transitions"
        if subcatselect == 6:
            subcatoption = "other"
        if subcatselect == 7:
            subcatoption = "slideshows"
        if subcatselect == 8:
            subcatoption = "intros"


        browser.get(startlink+midlink1 + "/?subcategories=" + subcatoption + "&page=1")
        time.sleep(1)

        listoflinks = []
        pageamount = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[2]/div[4]/div[2]/ul/li[9]/a').get_attribute("innerText")
        intpageamt = int(pageamount)

        linkn = 1
        for i in range(intpageamt):
            link = startlink + midlink1 +"/?subcategories=" + subcatoption + "&page=" + str(linkn)
            browser.get(link)
            time.sleep(2)

            sheet = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[2]/div[4]/div[1]')
            childn = 1
            print('Page ' + str(linkn) + ':')

            childele = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[2]/div[4]/div[1]').get_attribute("childElementCount")
            intchildele = int(childele)
            print(str(intchildele))
            for i in range(intchildele):
                xpath = "/html/body/div[2]/div/div[2]/div/div/div[2]/div[4]/div[1]/div[" + str(childn) + "]/div/div[1]/div/div/a"
                sheetchildren = browser.find_element(By.XPATH, xpath).get_attribute("href")
                print(sheetchildren)
                listoflinks.append(sheetchildren)
                childn = childn + 1

            print('\n')
            linkn = linkn + 1

        notepad.writelines('\n'.join(listoflinks))

    time.sleep(5)
    browser.quit()