from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import time


browser = webdriver.Chrome()
browser.maximize_window()

usernameStr = 'vishaladhithya19@gmail.com'
passwordStr = 'ironmansucks3000'


browser.get(('https://accounts.google.com/ServiceLogin/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=AddSession'))


username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 25).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(passwordStr)


signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()