import webbrowser
import subprocess
import tkinter as tk
from tkinter import messagebox


def try_launch_genshin():
    try:
        # 尝试启动原神，如果路径错误或程序无法运行，将引发异常
        subprocess.check_call(r"D:\Program Files\Genshin Impact\launcher.exe", shell=True)
    except subprocess.CalledProcessError as e:
        # 如果启动失败，则显示错误消息并提供下载链接
        messagebox.showerror("错误", "无法启动原神，请检查游戏路径是否正确。")
        webbrowser.open("https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default")
    except FileNotFoundError:
        # 如果文件未找到，也提供下载链接
        messagebox.showerror("错误", "未找到原神安装路径，您可以尝试重新安装或下载游戏。")
        webbrowser.open("https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default")
    except Exception as e:
        # 处理其他可能的异常
        messagebox.showerror("错误", f"发生未知错误: {e}")


def btnGoodbyeClicked():
    webbrowser.open("https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default")


top = tk.Tk()
top.geometry("400x200")
top.title("来玩原神好不好呀")

labelHello = tk.Label(top, text="欢迎使用原神启动器！")
labelHello.pack(pady=20)

btnLaunch = tk.Button(top, text="点我启动原神", command=try_launch_genshin)
btnLaunch.pack(pady=10)

btnDownload = tk.Button(top, text="无法启动？点击下载", command=btnGoodbyeClicked)
btnDownload.pack(pady=10)

top.mainloop()
