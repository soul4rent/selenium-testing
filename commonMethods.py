#An example of common methods for reference.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class CommonMethods:
    def waitUntilPageLoad(driver, webPage):
        driver.get(webPage)
        while driver.execute_script("return document.readyState") != "complete":
            print("not loaded")
            
        print("Web Page Loaded")

    def waitUntilElementExistsXPath(driver, webElement, timeout):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, webElement)))
    
        


driverPath = "chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
CommonMethods.waitUntilPageLoad(driver, "https://waluigi-bot.tumblr.com/")
