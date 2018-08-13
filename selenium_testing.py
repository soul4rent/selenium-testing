from selenium import webdriver

driver = webdriver.Chrome("C:\\Selenium\\Chrome\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.google.com")
driver.maximise_window()

print("hello")
