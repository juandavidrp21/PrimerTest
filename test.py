from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = 'C:\\dchrome\\chromedriver.exe'
driver= webdriver.Chrome()
driver.get("https://www.w3schools.com/")

original_window = driver.current_window_handle
assert len(driver.window_handles) == 1
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a.w3-button tut-button'.replace(' ','.'))))\
   .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.LINK_TEXT,'HTML Paragraphs')))\
   .click()

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.NAME,'ex1')))\
    .send_keys("<p>Hello World!</p>")

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#w3-exerciseform > div > button')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.number_of_windows_to_be((2)))\
    
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#answerbutton')))\
    .click()

