import tkinter as tk
from tkinter import messagebox
import time
import threading

# 定义弹出窗口的函数
def show_popup():
    # 创建主窗口
    root = tk.Tk()
    root.title("提醒")
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
            root.destroy()

    # 添加退出按钮
    button = tk.Button(root, text="退出", font=("微软雅黑", 30), command=close_window)
    button.pack(pady=20)
    # 运行主循环
    root.mainloop()

# 定义检测时间的函数
def check_time():
    while True:
        # 获取当前时间
        current_time = time.strftime("%H:%M", time.localtime())
        if current_time == "23:00":
            show_popup()  # 弹出窗口
            break  # 退出循环
        time.sleep(60)  # 每分钟检查一次

# 创建并启动线程
thread = threading.Thread(target=check_time)
thread.daemon = True  # 设置为守护线程，主程序退出时自动结束
thread.start()

# 主程序
print("程序已启动，请等待，不要关闭！")
# 保持主程序运行
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("程序已退出")
# show_popup()