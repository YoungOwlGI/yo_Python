import tkinter as tk
from tkinter import messagebox
import time
import threading
import ctypes

def show_popup():
    # 创建主窗口
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # 设置窗口为全屏
    # 设置窗口始终置顶
    root.attributes("-topmost", True)
    # 添加提示信息
    label = tk.Label(root, text="要睡觉啦！", font=("优设标题黑", 200), fg="red")
    label.pack(pady=20)
    label2 = tk.Label(root, text="现在是23:00，请立刻准备睡觉！", font=("微软雅黑", 70), fg="red")
    label2.pack(pady=20)
    # 定义退出按钮
    def close_window():
        # 退出提示
        if messagebox.askokcancel("提醒", "确定要退出吗？"):
            if messagebox.askokcancel("提醒", "确定要关闭窗口吗？"):
                root.destroy()
    # 添加退出按钮
    button = tk.Button(root, text="退出", font=("微软雅黑", 30), command=close_window)
    button.pack(pady=20)
    # 运行主循环
    root.mainloop()

def show_popup_l():
    # 创建主窗口
    root = tk.Tk()
    root.title("提醒")
    root.title("准备睡觉")
    root.geometry("600x300")
    root.attributes("-topmost", True)
    # 主程序
    label = tk.Label(root, text="要睡觉啦！", font=("千图小兔体", 70), fg="red")
    label.pack(pady=20)
    label2 = tk.Label(root, text="现在是22:45，请准备睡觉！", font=("微软雅黑", 30), fg="red")
    label2.pack(pady=20)

    root.mainloop()

def show_popup_r():
    """
    1. 锁屏
    """
    # 锁屏
    ctypes.windll.user32.LockWorkStation()
    # 解锁后 弹窗
    # 程序差不多和show_popup()一样
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes("-topmost", True)
    label = tk.Label(root, text="必须睡觉啦", font=("优设标题黑", 200), fg="red")
    label.pack(pady=20)
    label2 = tk.Label(root, text="现在是00:00，请立刻睡觉！", font=("微软雅黑", 70), fg="red")
    label2.pack(pady=20)
    def close_window():
        if messagebox.askokcancel("提醒", "确定要退出吗？"):
            root.destroy()
    button = tk.Button(root, text="退出", font=("微软雅黑", 30), command=close_window)
    button.pack(pady=20)
    root.mainloop()


# 定义检测时间的函数
def check_time():
    while True:
        # 获取当前时间
        current_time = time.strftime("%H:%M", time.localtime())
        if current_time == "22:45":
            show_popup_l()
        if current_time == "23:00":
            show_popup()
        if current_time == "00:00":
            show_popup_r()
            break  # 退出循环
        time.sleep(60)  # 每分钟检查一次

# 创建并启动线程
thread = threading.Thread(target=check_time)
thread.daemon = True  # 设置为守护线程，主程序退出时自动结束
thread.start()

print("程序已启动，请等待，不要关闭！")
# 保持主程序运行
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("程序已退出")

