from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://google.com")

# If element does not exist, crash webdriver in 5 seconds
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# Find first element in page which has class "gLYyf"
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# Clear elements before appending input
input_element.clear()

# Type in "hobbystation jp" and hit ENTER"
input_element.send_keys("hobbystation jp" + Keys.ENTER)

# Go to the website, finding the first anchor tag with ホビーステーションシングル通販店 / サイトTOP then clicking it
link = driver.find_element(By.PARTIAL_LINK_TEXT, "ホビーステーションシングル通販店 / サイトTOP")
link.click()

time.sleep(10)
driver.quit()


