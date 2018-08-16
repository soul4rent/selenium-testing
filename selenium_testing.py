from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def searchSite(webdriver, searchterm):
    driver.get("http://www.python.org")
    elem = driver.find_element_by_name("q") #finds searchbar
    elem.clear()
    elem.send_keys(searchterm)
    elem.send_keys(Keys.RETURN)

driver = webdriver.Chrome("C:\\Users\\Kyle\\Desktop\\chromedriver_win32\\chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
searchSite(driver, "test")
assert "No results found." not in driver.page_source
assert "test" in driver.page_source
print (driver.current_url)
driver.close()
