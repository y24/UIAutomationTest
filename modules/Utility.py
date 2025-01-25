import os
import re
import shutil
from urllib.parse import urlparse, urlunparse

# ディレクトリがなければ作成
def make_directory(dir_name:str):
    os.makedirs(dir_name, exist_ok=True)

# URLを分割して最後のディレクトリを取得
def get_url_last_directory(url:str, num:int):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.rstrip('/').split('/')
    return path_parts[num] if path_parts else None

# URLの最後のディレクトリ名(数字)をインクリメント
def increment_url_last_number(url:str):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.rstrip('/').split('/')
    if path_parts[-1].isdigit():
        path_parts[-1] = str(int(path_parts[-1]) + 1)
        new_path = '/'.join(path_parts) + '/'
    else:
        raise ValueError("URLの最後の部分が数字ではありません")
    new_url = urlunparse(parsed_url._replace(path=new_path))
    return new_url

# ディレクトリをZIPファイルに圧縮
def archive_directory(directory:str):
    zip_path = f"{directory}.zip"
    try:
        shutil.make_archive(directory, 'zip', directory)
        print(f"Create ZIP: {zip_path}")
        shutil.rmtree(directory)
        print(f"Delete Folder: {directory}")
    except Exception as e:
        print(f"Error: {e}")
        # エラー発生時、作成したzipファイルは削除
        if os.path.exists(zip_path):
            os.remove(zip_path)
    return zip_path

# ファイル名からWindowsで使用できない文字を削除
def sanitize_filename(filename:str):
    INVALID_CHARS = r'[\\/:*?"<>|]'
    return re.sub(INVALID_CHARS, '', filename)