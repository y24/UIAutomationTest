from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import urllib.parse

# ブラウザをセットアップ
def setup_driver(headless=False, remote_debug=False, page_load_strategy=False):
    options = Options()
    if headless:
        options.add_argument('--headless')  # ヘッドレスモード
    if remote_debug:
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  #リモートデバッグモードで起動したChromeに接続
    if page_load_strategy:
        options.page_load_strategy = 'none'  # ページ遷移時に読み込み完了まで待たない
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver

# テキスト取得
def get_text_by_xpath(driver, xpath:str):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return element.text

# 要素が現れるまで待機
def wait_by_xpath(driver, xpath:str):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

# 要素をクリック
def click_by_xpath(driver, xpath:str):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

# 次へ
def move_to_next(driver, xpath:str):
    next_url = driver.find_element(By.XPATH, xpath).get_attribute("href")
    driver.get(next_url)

# 画像を保存
def save_image(save_directory:str, driver, xpath:str, attr:str="src"):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    image_url = str(element.get_attribute(attr))
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            parsed_url = urllib.parse.urlparse(image_url)
            filename = str(os.path.basename(parsed_url.path))
            save_path = os.path.join(save_directory, filename)
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Saved: {save_path}")
        else:
            print(f"Save failed: {response.status_code} | {image_url}")