import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lista de tickers
s = ["AEAB11", "AEGPA9", "AESL17", "AESLA7"]

# Configuração do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)
url = "https://data.anbima.com.br/busca/debentures"

data = []

try:
    driver.get(url)
    driver.maximize_window()
    
    for ticker in s:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        search_box.clear()
        search_box.send_keys(Keys.CONTROL + "a")
        search_box.send_keys(Keys.DELETE)
        # time.sleep(1)
        search_box.send_keys(ticker)
        search_box.send_keys(Keys.RETURN)
        
        try:
            result_text = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/main/div/div/div/div/ul/li/div[3]/div[1]/dl/dd")
                )
            ).text
        except:
            result_text = "Não encontrado"
        
        data.append([ticker, result_text])
        # time.sleep(1)
        search_box.clear()

finally:
    driver.quit()

# Criar DataFrame e exibir tabela
df = pd.DataFrame(data, columns=["Código B3", "Setor"])
print(df.to_string(index=False))