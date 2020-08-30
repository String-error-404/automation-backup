from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import  time
import os
import webbrowser


usernameStr = 'vishaladhithya19@gmail.com'
passwordStr = 'ironmansucks3000'

browser = webdriver.Chrome()
browser.maximize_window()


browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

# fill in username and hit the next button

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(passwordStr)


signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()

# second tab 

browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")


browser.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F')

#drivr.get()
logonfacebook = browser.find_element_by_xpath('//*[@id="app"]/body/div[1]/div[2]/div/div[2]/div/a').click()



email = browser.find_element_by_id('email').send_keys('9941386141')

password = browser.find_element_by_id('pass').send_keys('flutterdev05')

sumbit = browser.find_element_by_xpath('//*[@id="loginbutton"]')
sumbit.click()



continueas = browser.find_element_by_xpath('//*[@id="u_0_10"]/div[2]/div[1]/div[1]/button')
continueas.click()

browser.get('https://open.spotify.com/')







