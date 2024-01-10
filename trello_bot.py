#1
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import os
import json

#2
CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "chromedriver.exe")
#Options for our web driver
# OP = webdriver.ChromeOptions()
# #add argument to it to OP
# OP.add_argument('--headless')
#3
DRIVER = webdriver.Chrome(CHROME_DRIVER_PATH)


def screenshotPage():
    time.sleep(2)
    date_str = date.today().strftime("%Y-%m-%d")
    fpath = os.path.join(os.getcwd(), 'screenshots{}.png'.format(date_str))
    DRIVER.get_screenshot_as_file(fpath)
    os.system(fpath)

#
def addTask():
    time.sleep(2)
    DRIVER.find_element(
        #first we need to click the add button
        By.XPATH, value="//button[contains(@class, 'O9vivwyDxMqo3q') and contains(@class, 'bxgKMAm3lq5BpA') and contains(@class, 'iUcMblFAuq9LKn') and contains(@class, 'PnEv2xIWy3eSui') and contains(@class, 'SEj5vUdI3VvxDc')]").click()
   #now we add data to the input,
    task_text_area = DRIVER.find_element(
        By.XPATH, value="//textarea[contains(@class, 'qJv26NWQGVKzI9')]")
    task_text_area.clear()
    task_text_area.send_keys("Walid Bot Added Task")
    #click again
    DRIVER.find_element(By.XPATH, value="//button[contains(@class, 'bxgKMAm3lq5BpA') and contains(@class, 'SdamsUKjxSBwGb') and contains(@class, 'SEj5vUdI3VvxDc')]").click()
    time.sleep(5)
#
#
def login():
    with open('config.json') as configFile:
        credentials = json.load(configFile) #load data fron the config file and then store it in a variable
        # print(credentials)

        time.sleep(2)
        #strategy and the value xml path is a locator, // is whole html
        DRIVER.find_element(By.XPATH,"//a[@data-uuid='MJFtCCgVhXrVl7v9HA7EH_login']").click()
        time.sleep(3)

        username = DRIVER.find_element(By.XPATH,"//input[@name='username']")
        print(username)
        #clear the input in case
        username.clear()
        #set the value of input to the one in json file
        username.send_keys(credentials["USERNAME"])
        DRIVER.find_element_by_css_selector("button[id='login-submit']").click()
        time.sleep(3)
        password = DRIVER.find_element_by_css_selector("input[name='password']")
        password.clear()
        password.send_keys(credentials["PASSWORD"])
        DRIVER.find_element_by_css_selector("button[id='login-submit']").click()


#         time.sleep(5)
#         password = DRIVER.find_element(
#             By.CSS_SELECTOR, value="input[name='password']")
#         password.clear()
#         password.send_keys(credentials["PASSWORD"])
#         time.sleep(5)
#         DRIVER.find_element_by_css_selector("button[type='submit']").click()
#
#
def navigateToBoard():
    time.sleep(5)
    DRIVER.find_element(
        By.XPATH, value="//div[@title='{}']/ancestor::a".format('Bot Board')).click()
    time.sleep(5)

#1
def main():
    #4 after argument
    try:
        #4 this will open the chrome and trello page
        DRIVER.get("https://trello.com")

        login()
        navigateToBoard()
        addTask()
        screenshotPage()
        input("Bot Operation Completed. Press any key...")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()


#1
if __name__ == "__main__":
    main()
