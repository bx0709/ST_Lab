from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"

driver.get(url)
select_element = Select(driver.find_element_by_xpath("//select[@name='continents']"))
time.sleep(5)

select_element.select_by_visible_text("Asia")
time.sleep(5)

select_element.select_by_index(0)
time.sleep(5)

driver.close()