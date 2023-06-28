from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# open test website
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()

# Scroll to YouTube - Send Feedback #
feedback = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[6]/div/ytd-guide-entry-renderer[4]/a")
driver.execute_script("return arguments[0].scrollIntoView();", feedback)
feedback.click()
sleep(3)
# Input feedback text
driver.find_element(By.CLASS_NAME, "scSharedMaterialtextfieldnative-control").send_keys("Yutub is oke. It's feeling good.")
sleep(3)
# click submit
driver.find_element(By.XPATH, "/html/body/div[1]/div/sc-shared-material-popup/div/div/div/uv-feedback-feedback-manager/div/div/div[1]/uv-feedback-form/div/div[4]/div/sc-shared-material-button/div/button").click()
sleep(3)
# click close
driver.find_element(By.XPATH, "/html/body/div[1]/div/sc-shared-material-popup/div/div/div/uv-feedback-feedback-manager/div/div/div[3]/uv-feedback-thank-you-page/div/div[3]/div/div[3]/sc-shared-material-button/div/button").click()
driver.close()
