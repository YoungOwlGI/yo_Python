import tkinter as tk  # 使用小写tk作为别名
from tkinter import messagebox  # 单独导入messagebox模块


def check_login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "youngowl" and password == "xiaomty":  # 替换为实际用户名和密码
        messagebox.showinfo("Login Status", "登录成功")  # 使用messagebox模块来调用showinfo
    else:
        messagebox.showinfo("Login Status", "用户名或密码错误")  # 使用messagebox模块来调用showinfo



app = tk.Tk()
app.title("Login")

tk.Label(app, text="Username:").pack()  # 使用Tk作为别名来创建Label
entry_username = tk.Entry(app)  # 使用Tk作为别名来创建Entry
entry_username.pack()

tk.Label(app, text="Password:").pack()  # 使用Tk作为别名来创建Label
entry_password = tk.Entry(app, show="*")  # 使用Tk作为别名来创建Entry
entry_password.pack()

button_login = tk.Button(app, text="Login", command=check_login)  # 使用Tk作为别名来创建Button
button_login.pack()

app.mainloop()