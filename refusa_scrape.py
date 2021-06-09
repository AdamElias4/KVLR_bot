from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob
import os
import time
import random

def original_bot(url, start, end, state_abbrev):

    PATH = "/Users/adamelias/Downloads/chromedriver" # change 'mitchellpolozov' to the user associated with your computer!
    driver = webdriver.Chrome(PATH)

    driver.get(url)
    time.sleep(5)

    user = driver.find_element_by_name("name")
    user.send_keys("PACREG2076036")

    pin = driver.find_element_by_name("user_pin")
    pin.send_keys("1718")
    pin.send_keys(Keys.RETURN)

    time.sleep(15)

    pages = end - start

    for i in range(pages):
        captchaPresent = len(driver.find_elements_by_name('ResultViews.Attempt')) > 0

        if captchaPresent:
            add_box = driver.find_element_by_name('ResultViews.Attempt')
            add_box.send_keys("7")
            continu = driver.find_element_by_xpath("//span[text() = 'Continue']")
            continu.click()

        selector = driver.find_element_by_id('checkboxCol')
        selector.click()
        page = driver.find_element_by_xpath('//*[@class = "next button mousedown-enterkey"]')
        page.click()
        time.sleep(random.randint(5, 10))

    download = driver.find_element_by_xpath('//*[@class = "action download action-download"]')
    download.click()

    time.sleep(15)
    custom = driver.find_element_by_id('detailCustom')
    custom.click()

    Record_type_unselect = driver.find_element_by_xpath('//*[contains(text(), "Record Type")]').click()
    Fax_num = driver.find_element_by_xpath('//*[contains(text(), "Fax Number Combined")]').click()
    Phone_num = driver.find_element_by_xpath('//*[contains(text(), "Phone Number Combined")]').click()
    website = driver.find_element_by_xpath('//*[contains(text(), "Website")]').click()
    Location_sales = driver.find_element_by_xpath('//*[contains(text(), "Location Sales Volume Actual")]').click()
    EIN_1 = driver.find_element_by_xpath('//*[contains(text(), "EIN 1")]').click()
    EIN_2 = driver.find_element_by_xpath('//*[contains(text(), "EIN 2")]').click()
    EIN_3 = driver.find_element_by_xpath('//*[contains(text(), "EIN 3")]').click()
    Linked_in = driver.find_element_by_xpath('//*[contains(text(), "Linked-In")]').click()

    download_records = driver.find_element_by_xpath(
        '//*[@class= "originButton ui-priority-primary view-on-exportlimit view-on-randomsample action-download"]').click()

    time.sleep(10)

    folder = glob.glob('/Users/adamelias/Downloads/*.csv') # change 'mitchellpolozov' to the user associated with your computer!
    newest_file = max(folder, key=os.path.getctime)

    end = end - 1

    # Deals with the last scrape of the state where the page number
    # is not divisible by 20

    while end % 20 != 0:
        end += 1

    os.rename(newest_file, str(end) + state_abbrev + 'RefUSA.csv')

    # prints to console to confirm the file was created
    print(str(end) + state_abbrev + 'RefUSA.csv file successfully created')

    driver.quit()

