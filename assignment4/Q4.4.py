from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("https://google.com")
    
js = '''
var name = prompt("This is invoked Javascript. What's your name:")
alert("Hey " + name)
'''
driver.execute_script(js)
    
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")