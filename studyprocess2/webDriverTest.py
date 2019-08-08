#有问题，没有好
from selenium import webdriver

chromedriver="/usr/local/lib/python3.7/site-packages/selenium/webdriver/safari"
driver=webdriver.Safari(chromedriver)
driver.get('http://www.baidu.com')