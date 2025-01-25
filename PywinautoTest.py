from pywinauto import Desktop
from pywinauto.timings import wait_until

def find_control_by_text(controls, text:str):
    for ctrl in controls:
        if ctrl.window_text() == text:
            return ctrl

# Desktop オブジェクトの作成
desktop = Desktop(backend="uia")
# desktop = Desktop(backend="win32")

# 特定のウィンドウをタイトルで取得
windows = desktop.windows(title="電卓")
# windows = desktop.windows(title_re=".*メモ帳.*")

# 取得したウィンドウの数を表示
print(f"Window Count: {len(windows)}")

# 各ウィンドウを操作
for i, window in enumerate(windows):
    print(f"\nWindow {i + 1}: title={window.window_text()}, handle={window.handle}")

    # ウィンドウにフォーカス
    window.set_focus()

    # win32
    # window.print_control_identifiers()

    #uia
    controls = window.descendants()
    
    # クリック
    inputs = ["ナビゲーションを開く", "2", "3"]
    target = find_control_by_text(controls, inputs[i])
    target.click()

    for ctrl in controls:
        print(f"Control: {ctrl.window_text()}")