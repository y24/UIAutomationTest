from pywinauto import Application, Desktop

def launch_app(path:str, backend="win32"):
    """パスを指定してアプリを起動"""
    return Application(backend=backend).start(path)


def connect_app(title:str, backend="win32", exact=False):
    """タイトルを指定して起動済みのアプリに接続"""
    if exact:
        return Application(backend=backend).connect(title=title)
    else:
        return Application(backend=backend).connect(title_re=title)


def get_windows_from_desktop(title:str, backend="win32", exact=False):
    """デスクトップから合致するタイトルのウインドウを取得"""
    desktop = Desktop(backend=backend)
    if exact:
        return desktop.windows(title=title)
    else:
        return desktop.windows(title_re=title)


def get_window_from_app(app, title:str, exact=False):
    """アプリケーション上のウインドウを取得"""
    if exact:
        return app.window(title=title)
    else:
        return app.window(title_re=title)


def wait(window):
    """ウインドウが利用可能になるまで待機"""
    window.wait("enabled", timeout=30)


def print_controls(controls):
    """descendants()で取得した要素の情報を出力"""
    for ctrl in controls:
        print(f"[{ctrl.control_id()}]{ctrl.friendly_class_name()} : {ctrl.window_text()}")


def find_element_by_text(controls, text:str):
    """descendants()で取得した要素をテキストで検索して、1番目にマッチしたものを取得"""
    for ctrl in controls:
        if ctrl.window_text() == text:
            return ctrl


def find_elements_by_classname(controls, classname:str):
    """descendants()で取得した要素をClass名で検索して、マッチしたものを全て取得"""
    return [ ctrl for ctrl in controls if ctrl.friendly_class_name() == classname]
