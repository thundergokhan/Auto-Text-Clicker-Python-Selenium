from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Web driver'ı başlat
driver = webdriver.Chrome()

# Sayfayı yükle
driver.get("https://www.google.com/")

# Arama kutusunu bul
search_box = driver.find_element(By.NAME, "q")

# Arama kutusuna yazı gönder
search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

# Arama sonuçları sayfasının yüklenmesini bekle
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

# İlk sonuca tıkla
first_result = driver.find_element(By.CSS_SELECTOR, "div.g a")
first_result.click()

# Web sürücüsünü kapat
driver.quit()
