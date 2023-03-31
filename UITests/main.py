from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
#driver.get('https://www.google.com')
driver.get('http://localhost/')


print(driver.title)


button1 = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div.Keypad > table > tbody > tr:nth-child(3) > td:nth-child(1) > button')
button1.click()

buttonadd = driver.find_element(By.ID, 'add')
buttonadd.click()

button2 = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div.Keypad > table > tbody > tr:nth-child(3) > td:nth-child(2) > button')
button2.click()

time.sleep(1)

buttonEqual = driver.find_element(By.NAME, 'equal')
buttonEqual.click()

buttonMultiply = driver.find_element(By.CLASS_NAME, 'Multiply')
buttonMultiply.click()

button2.click()

time.sleep(1)


buttonEqual.click()

time.sleep(1)

result = driver.find_element(By.CLASS_NAME, 'DisplayText')
print(result.get_attribute('value'))

if(result.get_attribute('value') == '6'):
    print('Test passed')
else:
    print('Test failed expected: 6 actual: ' + result.get_attribute('value'))

