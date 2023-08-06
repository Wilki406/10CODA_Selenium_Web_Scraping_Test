from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
url = 'C:/Users/Kille/Documents/2022/2022 Semester 2/Stem & Computing/COMPUTING/SeleniumTask/selenium_task/timvroomclone.html'
driver.get(url)

title = driver.title
driver.find_element(By.ID,'pagetitle').send_keys(title)
driver.find_element(By.ID, 'uname').send_keys("Mr_Fitz")
occupation_dropdown = Select(driver.find_element(By.ID, 'favsubject'))
occupation_dropdown.select_by_index(2)
driver.find_element(By.XPATH, '//*[@id="testform"]/input[4]').click()
driver.find_element(By.ID, 'submitbutton').click()
bbcount = len(driver.find_elements(By.CLASS_NAME, 'blackbox'))
driver.find_element(By.ID, 'answer7').send_keys(bbcount)
num8 = driver.execute_script("return ran_that_js_function()")
print(num8)

driver.find_element(By.ID, 'pass').send_keys("surelyitcouldntbethateasy")

purplebox = driver.find_element(By.ID, 'rbox')
answer14 = driver.find_element(By.ID, 'answer9')
if purplebox.is_displayed():
    answer14.send_keys('yes')
else:
    answer14.send_keys('no')

ActionChains(driver).move_to_element(driver.find_element(By.ID, 'bottom')).perform()