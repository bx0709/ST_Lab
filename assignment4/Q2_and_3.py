from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.facebook.com")

title = driver.title
print(title)

u= driver.find_element_by_id('email')
u.send_keys("bhavya3217@yahoo.com")
u = driver.find_element_by_id('pass')
u.send_keys("happy123")
login = driver.find_element_by_name('login')
login.click()
