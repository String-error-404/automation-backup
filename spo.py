from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import  time
import os




driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F')

#drivr.get()
logonfacebook = driver.find_element_by_xpath('//*[@id="app"]/body/div[1]/div[2]/div/div[2]/div/a').click()



email = driver.find_element_by_id('email').send_keys('9941386141')

password = driver.find_element_by_id('pass').send_keys('flutterdev05')

sumbit = driver.find_element_by_xpath('//*[@id="loginbutton"]')
sumbit.click()

time.sleep(10)

continueas = driver.find_element_by_xpath('//*[@id="u_0_10"]/div[2]/div[1]/div[1]/button')
continueas.click()

driver.get('https://open.spotify.com/')


# driver.findElement(By.id("email")).sendKeys("youremail@example.com")
# driver.findElement(By.id("pass")).sendKeys("password")

# driver.findElement(By.id("loginbutton")).click()