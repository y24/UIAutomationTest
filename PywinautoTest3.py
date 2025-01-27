from modules import PywinautoWrapper as Pwa

# Logger
from modules import Logger
logger = Logger.get_logger(__name__, console=True, file=False, trace_line=False)

# アプリケーションのパス
app_path = r"C:\Windows\system32\notepad.exe"

# 入力文字
arr = ["abcdef", "ghijklm"]

try:
    # 指定数だけ複数起動
    for i in range(len(arr)):
        # 起動
        app = Pwa.launch_app(app_path)
        window = Pwa.get_window_from_app(app, title=".*メモ帳.*", exact=False)

        # 待機
        Pwa.wait(window)
        logger.info(window.print_control_identifiers())

        # 要素を取得
        controls = window.descendants()
        Pwa.print_controls(controls)

        # ウィンドウにフォーカス
        window.set_focus()

        # 入力
        edit = Pwa.find_elements_by_classname(controls, "Edit")
        edit[0].type_keys(arr[i])

        # クリック
        # button = Pwa.find_element_by_text(controls, "元に戻す(&U)")
        # button.click()

except Exception as e:
    logger.error(e)
