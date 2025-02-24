import subprocess
import tkinter as tk


def btnHelloClicked():
    labelHello.config(text="来吧，随我一起启动 崩坏:星穹铁道 吧！")
    subprocess.Popen(r"D:\Program Files\Star Rail\launcher.exe", shell=True)


top = tk.Tk()
top.geometry("1080x900")
top.title("小猫头鹰")
labelHello = tk.Label(top, text="崩坏:星穹铁道，启动！！！\n Honkai Star Rail,RUN!!!", height=25, width=200, fg="blue",
                      font="微软雅黑,1500")
labelHello.pack()
btn = tk.Button(top, text="启动！！！", command=btnHelloClicked)
btn.pack()
top.mainloop()
