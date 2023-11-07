import os
import shutil
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def make_folder(name: str) -> None:

    if not os.path.isdir(name):
        os.mkdir(name)


def get_hyperlinks(request: str) -> None:

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    url = f"https://yandex.ru/images/search?text={request}"
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(
        By.CSS_SELECTOR, 'div.serp-item__preview a.serp-item__link').click()

    with open(f"urls_{request}.txt", 'w') as file:
        for i in range(1200):
            try:
                time.sleep(0.5)
                link = driver.find_element(
                    By.CSS_SELECTOR, "a.Button2_view_action").get_attribute("href")
                file.write(link + '\n')
                driver.find_element(
                    By.CSS_SELECTOR, "div.CircleButton:nth-child(4)").click()
            except:
                continue

    driver.close()
    driver.quit()


def download_img(request: str) -> None:
    count = 0
    make_folder("dataset")
    make_folder(f"dataset/{request}")

    with open(f"urls_{request}.txt", "r") as file:
        for line in file:
            try:
                url = line.strip()
                time.sleep(4)
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    count += 1
                    with open(f"dataset/{request}/{str(count).zfill(4)}.jpg", "wb") as image_file:
                        shutil.copyfileobj(response.raw, image_file)
                else:
                    continue
            except:
                continue
    print(f'{count} успешно скачано')


def main() -> None:
    if os.path.isdir("dataset"):
        shutil.rmtree("dataset")

    request = "bay_horse"
    get_hyperlinks(request)
    download_img(request)

    request = "zebra"
    get_hyperlinks(request)
    download_img(request)