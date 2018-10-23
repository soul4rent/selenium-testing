#An example of common methods for reference.
from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class CommonMethods:
    def waitUntilPageLoad(driver, webPage):
        driver.get(webPage)
        while driver.execute_script("return document.readyState") != "complete":
            print("not loaded")
            
        print("Web Page Loaded")
        
        


driverPath = "chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
CommonMethods.waitUntilPageLoad(driver, "https://waluigi-bot.tumblr.com/")
