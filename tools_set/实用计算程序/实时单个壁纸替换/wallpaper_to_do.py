import os
import time
import platform
from pathlib import Path
from PIL import Image  # 用于验证图片有效性


def set_wallpaper(img_path):
    """设置壁纸（跨平台支持）"""
    img_path = str(Path(img_path).absolute())

    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3)
    elif platform.system() == "Darwin":
        import subprocess
        script = f'tell application "System Events" to set picture of every desktop to "{img_path}"'
        subprocess.run(["osascript", "-e", script])
    elif platform.system() == "Linux":
        if "GNOME" in os.getenv("XDG_CURRENT_DESKTOP", ""):
            os.system(f"gsettings  set org.gnome.desktop.background  picture-uri file://{img_path}")
        elif "KDE" in os.getenv("XDG_CURRENT_DESKTOP", ""):
            os.system(f"plasma-apply-wallpaperimage  {img_path}")


def monitor_single_file(file_path):
    """监控单个文件的修改时间变化"""
    last_mtime = 0
    while True:
        try:
            current_mtime = os.path.getmtime(file_path)
            if current_mtime != last_mtime:
                # 验证是否为有效图片（可选）
                try:
                    with Image.open(file_path) as img:
                        img.verify()
                    set_wallpaper(file_path)
                    print(f"壁纸已更新: {time.strftime('%H:%M:%S')}")
                    last_mtime = current_mtime
                except (IOError, SyntaxError):
                    print("错误：文件不是有效图片")
        except FileNotFoundError:
            print("错误：文件不存在，等待重新检测...")

        time.sleep(1)  # 每秒检查一次


if __name__ == "__main__":
    target_file = "D:\猫头鹰的文件\保留文件\Wallpaper.png"  # 替换为你的图片绝对路径
    print(f"开始监控文件: {target_file}")
    monitor_single_file(target_file)