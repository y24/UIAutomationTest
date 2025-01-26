from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from modules import WebDriver as WD
from modules import Logger

# Chromeをリモートデバッグモードで起動しておく
# cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrome-debug"

# Logger
logger = Logger.get_logger(__name__, console=True, file=False, trace_line=False)

try:
    # WebDriverセットアップ
    driver = WD.setup_driver(headless=False, remote_debug=True, page_load_strategy=True)
    logger.info("Start WebDriver")

    # 検索クエリ
    queries = ["bbb", "ccc", "ddd", "fff"]

    # 全タブを取得
    all_tabs = driver.window_handles
    logger.debug(f"Tab Handles: {all_tabs}")

    # 各タブを操作(検索)
    for index, query in enumerate(queries):
        # タブを切り替え
        target_tab = all_tabs[index]
        driver.switch_to.window(target_tab)
        logger.debug(f"Tab {index}: {target_tab}")

        # Googleに移動
        driver.get("https://www.google.co.jp")

        # 検索窓
        xpath = '//textarea[@title="検索"]'
        search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        # 検索
        query = queries[index]
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        logger.debug(f"Search: {query}")

        # 検索結果の一番上のリンクを出力
        search_result = WD.get_text_by_xpath(driver, '//h3')
        logger.debug(f"Result: {search_result}")

    # 各タブを操作(リンククリック)
    for tab_handle in all_tabs:
        # タブを切り替え
        driver.switch_to.window(tab_handle)

        # 検索結果の一番上をクリック
        link = driver.find_element(By.XPATH, '//h3')
        link.click()

except Exception as e:
    logger.error(e)