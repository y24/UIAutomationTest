from modules import PywinautoWrapper as Pwa

# Logger
from modules import Logger
logger = Logger.get_logger(__name__, console=True, file=False, trace_line=False)

# 特定のウィンドウをタイトルで取得
windows = Pwa.get_windows_from_desktop(title=".*メモ帳.*", backend="win32", exact=False)

# 取得したウィンドウの数を表示
logger.info(f"Window Count: {len(windows)}")

try:
    # 各ウィンドウを操作
    for i, window in enumerate(windows):
        logger.info(f"Window {i + 1}: title={window.window_text()}, handle={window.handle}")

        # 要素を取得
        controls = window.descendants()
        Pwa.print_controls(controls)

        # ウィンドウにフォーカス
        window.set_focus()

        # 入力
        edit = Pwa.find_elements_by_classname(controls, "Edit")
        edit[0].type_keys("abcdefg")

        # クリック
        # button = Pwa.find_element_by_text(controls, "元に戻す(&U)")
        # button.click()

except Exception as e:
    logger.error(e)
