from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import  time
import os
import webbrowser


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/")
signin = driver.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > a.HeaderMenu-link.no-underline.mr-3')
signin.click()
username = driver.find_element_by_css_selector('#login_field')
username.send_keys('Vishal-Adhithya')
password = driver.find_element_by_css_selector('#password')
password.send_keys('flutterdev05')
submit = driver.find_element_by_css_selector('#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block')
submit.click()