from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Start the web driver
driver = webdriver.Chrome()

# Load the page
driver.get("https://www.google.com/")

# Find the search box
search_box = driver.find_element(By.NAME, "q")

# Send text to the search box
search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

# Wait for the search results page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

# Click on the first result
first_result = driver.find_element(By.CSS_SELECTOR, "div.g a")
first_result.click()

# Close the web driver
driver.quit()
