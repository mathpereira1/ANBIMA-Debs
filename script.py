import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = ["AEAB11", "AEGPA9", "AESL17", "AESLA7"]
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")  # Resolução de desktop

driver = webdriver.Chrome(options=chrome_options)

url = "https://data.anbima.com.br/busca/debentures"
print("Código B3 --- Setor")
try:
    driver.get(url)
    driver.maximize_window()
    for ticker in s:
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
        search_box.clear()
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.DELETE)
        time.sleep(1)
        search_box.send_keys(ticker)
        search_box.send_keys(Keys.RETURN)
        result_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div/div/ul/li/div[3]/div[1]/dl/dd"))).text        
        print(f"{ticker}: {result_text}")
        time.sleep(1)
        search_box.clear()

finally:
    driver.quit()