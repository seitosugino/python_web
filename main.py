from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.google.com/')