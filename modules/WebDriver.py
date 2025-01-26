from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import urllib.parse

# タイムアウト秒数
TIMEOUT = 10


def setup_driver(headless=False, remote_debug=False, page_load_strategy=False):
    """Setup Webdriver"""
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


def get_text_by_xpath(driver, xpath:str):
    """XPATHを指定してinnerTextを取得"""
    element = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return element.text


def wait_by_xpath(driver, xpath:str):
    """XPATHを指定して要素がクリック可能になるまで待機"""
    element = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return element


def click_by_xpath(driver, xpath:str):
    """XPATHを指定して要素をクリック"""
    element = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
    return element


def move_to_href(driver, xpath:str):
    """XPATHを指定して要素からhrefを取得して移動"""
    href = driver.find_element(By.XPATH, xpath).get_attribute("href")
    driver.get(href)
    return href


def save_img_src(save_directory:str, driver, xpath:str, attr:str="src"):
    """XPATHを指定して画像を保存"""
    element = WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    image_url = str(element.get_attribute(attr))
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            parsed_url = urllib.parse.urlparse(image_url)
            filename = str(os.path.basename(parsed_url.path))
            save_path = os.path.join(save_directory, filename)
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Saved: {filename}")
            return save_path
        else:
            print(f"Save failed: {response.status_code} | {image_url}")
            return None