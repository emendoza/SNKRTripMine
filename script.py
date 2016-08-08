from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os, sys
import time

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
url = raw_input("URL: ")
size = raw_input("Size: ")
window = raw_input("Input How Long to Watch (in minutes):")
window = 20 * int(window)

print "==================="
driver = webdriver.Chrome('C:\MiscPrograms\ChromeDriver\chromedriver.exe');
driver.get(url)
dropdownDiv = 0
selectList = 0
submitButton = 0

for x in range(window):
	try:
		dropdownDiv = driver.find_element_by_class_name('exp-pdp-size-container')
		selectList = driver.find_element_by_class_name('exp-pdp-size-dropdown-container')
		submitButton = driver.find_element_by_id('buyingtools-add-to-cart-button')
		break
	except:
		time.sleep(3)
		driver.refresh()
		print "Refreshed " + x + " times"

if selectList == 0 or dropdownDiv == 0 or submitButton == 0:
	sys.exit()

dropdownDiv.click()
for option in selectList.find_elements_by_tag_name('li'):
	if option.text == size:
		option.click()
		break
submitButton.click()
print "Successfully added to cart"
