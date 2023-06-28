from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get(url="https://www.google.com/")
driver.maximize_window()
sleep(3)
search = driver.find_element(By.NAME, "q")
search.send_keys("sanbercode")
search.send_keys(Keys.RETURN)
sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "Sanbercode - Online Learning & Bootcamp").click()
sleep(3)
page_title = driver.title
if page_title == "Sanbercode - Online Learning & Bootcamp":
    assert True
    driver.save_screenshot("./screenshot/landing_page.png")
else:
    print("Page error")
    driver.close()
