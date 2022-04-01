import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.amazon.in/"
driver.get(url)

select_element  = driver.find_element_by_id('searchDropdownBox')
select_object  = Select(select_element)

all_available_options = select_object.options

for element in all_available_options:
    print(element.text)
    
print()

time.sleep(4)
driver.close()