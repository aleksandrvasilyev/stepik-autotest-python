from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome('/usr/local/bin/chromedriver')
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 300);")
button.click()