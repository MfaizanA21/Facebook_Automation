import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.facebook.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

loginMail = wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
loginMail.click()
loginMail.send_keys('youremail@gmail.com')

loginPassword = wait.until(ec.visibility_of_element_located((By.NAME, 'pass')))
loginPassword.click()
loginPassword.send_keys('yourPassword')

loginButton = wait.until(ec.element_to_be_clickable((By.NAME, 'login')))
loginButton.click()

time.sleep(10)
driver.get('https://www.facebook.com/pages/')

time.sleep(5)

driver.get('https://www.facebook.com/pages/creation/')

pageName = wait.until(ec.presence_of_all_elements_located((By.ID, ':r20:')))
pageName.send_keys('Test Page')
time.sleep(5)
pageCategory = wait.until(ec.visibility_of_element_located((By.ID, ':r20:')))
pageCategory.click()
pageCategory.send_keys('Education')