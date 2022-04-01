from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

url = "https://demoqa.com/select-menu"

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get(url)
print("Opened website")
sleep(1)


dropdown_box = driver.find_element_by_xpath("//select[@id='oldSelectMenu']/option[text()='Green']")
dropdown_select = dropdown_box.click()
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")