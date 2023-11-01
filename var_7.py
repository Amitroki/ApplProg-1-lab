import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def get_hyperlinks(request): 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  
    url = f"https://yandex.ru/images/search?text={request}"
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, 'div.serp-item__preview a.serp-item__link').click()

    path = f"urls_{request}.txt"
    path_to_the_folder = "C:\\Users\\Alex\\Desktop\\urls" + path
    with open(path_to_the_folder, 'w') as file:
        for i in range(15):
            time.sleep(0.3)
            link = driver.find_element(By.CSS_SELECTOR, "a.Button2_view_action").get_attribute("href")
            file.write(link + '\n')
            driver.find_element(By.CSS_SELECTOR, "div.CircleButton:nth-child(4)").click()

    driver.close()
    driver.quit()

def main():
    request = "bay_horse"
    get_hyperlinks(request)

if __name__ == "__main__":
    main()