from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# identify dropdown with Select class
sel = Select(driver.find_element_by_xpath("//select[@name='continents']"))
#select by select_by_visible_text() method
time.sleep(5)
sel.select_by_visible_text("Europe")
time.sleep(5)
#select by select_by_index() method
sel.select_by_index(0)
time.sleep(5)
driver.close()