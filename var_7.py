import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def get_hyperlinks(request): 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  
    url = f"https://yandex.ru/images/search?text={request}"
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, 'div.serp-item__preview a.serp-item__link').click()

    path = f"urls_{request}.txt"
    path_to_the_folder = "C:\\Users\\Alex\\Desktop\\" + path
    with open(path_to_the_folder, 'w') as file:
        for i in range(10):
            try:
                time.sleep(0.5)
                link = driver.find_element(By.CSS_SELECTOR, "a.Button2_view_action").get_attribute("href")
                file.write(link + '\n')
                driver.find_element(By.CSS_SELECTOR, "div.CircleButton:nth-child(4)").click()
            except:
                continue

    driver.close()
    driver.quit()

def download_img(request):
    count = 0
    os.makedirs(f"dataset/{request}")

    with open(f"urls_{request}.txt", "r") as file:
        for line in file:
            try:
                url = line.strip()
                time.sleep(4)
                response = requests.get(url)
                if response.status_code == 200:
                    with open(f"dataset/{request}/{count}.jpg", "wb") as image_file:
                        image_file.write(response.content)
                    count+=1
                else:
                    print(f'Ошибка при скачивании изображения с URL: {url}')
            except:
                continue

def main():
    request = "bay_horse"
    get_hyperlinks(request)
    download_img(request)

if __name__ == "__main__":
    main()