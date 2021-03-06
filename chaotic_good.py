from selenium import webdriver #importing everything until I know what I need during dev.
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import random

driverPath = "chromedriver_win32\\chromedriver.exe"
options = Options()  
options.add_argument("--headless")

rice_grains = 0


while True:

    driver = webdriver.Chrome(driverPath)
    #driver = webdriver.Chrome(driverPath, options=options)
    driver.get("http://freerice.com/")
    try:
        while "rice_blocked" not in driver.page_source:
            xpath = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//a[@rel={random.randint(0,3)}]"))
            )

            src = driver.page_source
            xpath.click()

            #wait until question answered
            while True:
                print(1)
                if "Correct!" or "Incorrect!" in driver.page_source:
                    break
            
            if "Correct!" in driver.page_source:
                rice_grains += 10
                print(f"Success! Rice Grains Donated: {rice_grains}")
            else:
                print("Guess and check failed!")

            #wait until page finished updating
            while True:
                print(2)
                if driver.page_source != src:
                    break

            time.sleep(.5)
    except:
        print("FAILURE. RESTARTING:")
    driver.quit()
    
