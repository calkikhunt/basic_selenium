from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()  
driver.get("https://www.google.com/")


search_box = driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']")
search_box.send_keys('Hello')
search_box.submit()

