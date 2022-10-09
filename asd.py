from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = 'https://bookread.com.ua/search/'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.CLASS_NAME, 'mr-1')
    input1.send_keys("жизнь")

    input2 = browser.find_element(By.CLASS_NAME, 'btn')
    input2.click()

finally:
    time.sleep(3)
    browser.quit()