import tkinter as tk
from tkinter import messagebox
import time
import ctypes


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口
        self.active = True  # 程序运行状态标志
        self.schedule_check()

    def show_popup(self):
        top = tk.Toplevel()
        top.attributes('-fullscreen', True)
        top.attributes("-topmost", True)

        label = tk.Label(top, text="要睡觉啦！", font=("优设标题黑", 200), fg="red")
        label.pack(pady=20)

        label2 = tk.Label(top, text="现在是23:00，请立刻准备睡觉！", font=("微软雅黑", 70), fg="red")
        label2.pack(pady=20)

        def close_window():
            if messagebox.askokcancel("提醒", "确定要退出吗？") and messagebox.askokcancel("提醒", "确定要关闭窗口吗？"):
                top.destroy()

        button = tk.Button(top, text="退出", font=("微软雅黑", 30), command=close_window)
        button.pack(pady=20)

    def show_popup_l(self):
        top = tk.Toplevel()
        top.title("提醒")
        top.geometry("600x300")
        top.attributes("-topmost", True)

        label = tk.Label(top, text="要睡觉啦！", font=("千图小兔体", 70), fg="red")
        label.pack(pady=20)

        label2 = tk.Label(top, text="现在是22:45，请准备睡觉！", font=("微软雅黑", 30), fg="red")
        label2.pack(pady=20)

    def show_popup_r(self):
        ctypes.windll.user32.LockWorkStation()
        top = tk.Toplevel()
        top.attributes('-fullscreen', True)
        top.attributes("-topmost", True)

        label = tk.Label(top, text="必须睡觉啦", font=("优设标题黑", 200), fg="red")
        label.pack(pady=20)

        label2 = tk.Label(top, text="现在是00:00，请立刻睡觉！", font=("微软雅黑", 70), fg="red")
        label2.pack(pady=20)

        def close_window():
            if messagebox.askokcancel("提醒", "确定要退出吗？"):
                top.destroy()
                self.stop_program()

        button = tk.Button(top, text="退出", font=("微软雅黑", 30), command=close_window)
        button.pack(pady=20)

    def check_time(self):
        if not self.active:
            return

        current_time = time.strftime("%H:%M")
        print(f"当前时间: {current_time}")  # 调试用

        if current_time == "22:45":
            self.show_popup_l()
        elif current_time == "23:00":
            self.show_popup()
        elif current_time == "00:00":
            self.show_popup_r()
            self.stop_program()
            return

        # 每分钟检查一次（使用Tkinter定时器）
        self.root.after(60000, self.check_time)

    def stop_program(self):
        self.active = False
        self.root.destroy()

    def schedule_check(self):
        self.check_time()
        self.root.mainloop()


if __name__ == "__main__":
    app = App()