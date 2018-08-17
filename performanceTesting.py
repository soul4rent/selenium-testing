from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

caps = DesiredCapabilities.CHROME #capabilities
caps['loggingPrefs'] = {'performance': 'ALL'}

driverPath = "C:\\Users\\Kyle\\SelfProgrammingProjects\\selenium-experimentation\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(driverPath, desired_capabilities=caps)
driver.get('http://www.google.com')

#list comprehensions for json logs
logs = [json.loads(log['message'])['message'] for log in driver.get_log('performance')]
print(json.dumps(logs))
