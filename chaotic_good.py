from selenium import webdriver #importing everything until I know what I need during dev.
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

driverPath = "chromedriver_win32\\chromedriver.exe"
options = Options()  
options.add_argument("--headless")

rice_grains = 0

#driver = webdriver.Chrome(driverPath)
while True:
    driver = webdriver.Chrome(driverPath, options=options)
    driver.get("http://freerice.com/")
    try:
        while "rice_blocked" not in driver.page_source:
            xpath = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@rel='0']"))
            )
            xpath.click()

            #wait until question answered
            while True:
                if "Correct!" or "Incorrect!" in driver.page_source:
                    break
            
            if "Correct!" in driver.page_source:
                rice_grains += 10
                print(f"Success! Rice Grains Donated: {rice_grains}")
            else:
                print("Guess and check failed!")
            time.sleep(1)
    except:
        print("FAILURE. RESTARTING:")
    driver.quit()
    
