# A bot to send a tweet 
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://twitter.com/login?lang=ar')
username = driver.find_element_by_name('session[username_or_email]')
username.clear()
username.send_keys("")
password = driver.find_element_by_name('session[password]')
password.clear()
password.send_keys('')
password.submit()
driver.implicitly_wait(10)
tweett = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
tweett.send_keys('This tweet is from Python')
send_tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
send_tweet.click()
time.sleep(120)
driver.quit()