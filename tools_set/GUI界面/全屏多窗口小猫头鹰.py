import random
import tkinter as tk
import webbrowser
from tkinter import font

def close_main_window():
    root.destroy()

def open_search_page():
    url = "https://cn.bing.com/?mkt=zh-CN"
    webbrowser.open(url, new=0, autoraise=True)

def generate_random_color():
    # 生成一个随机的十六进制颜色代码
    return f'#{random.randint(0, 0xFFFFFF):06X}'

def create_random_color_window(text):
    toplevel = tk.Toplevel(root)
    toplevel.title("小猫头鹰")
    ys_color = generate_random_color()
    toplevel.configure(bg=ys_color)

    label_font = font.Font(size=16, weight='bold')
    tk.Label(toplevel, text=text, bg=ys_color, font=label_font, wraplength=280, fg="white").pack(pady=20)

    # 关闭小窗口的按钮
    close_button = tk.Button(toplevel, text="关闭窗口", command=toplevel.destroy, bg='lightgray', font=font.Font(size=12))
    close_button.pack(pady=10)

    x = random.randint(0, idth - 300)
    y = random.randint(0, eight - 200)
    toplevel.geometry(f"300x200+{x}+{y}")

def yoowl():
    i = int(input("请输入要创建的窗口数量："))
    for i in range(i):  # 创建6个窗i口
        create_random_color_window(random.choice(love_bq))

# 主窗口设置
root = tk.Tk()
root.title("小猫头鹰碎碎念")

# 获取屏幕分辨率
idth = root.winfo_screenwidth()
eight = root.winfo_screenheight()
x = int(idth / 2) - 150
y = int(eight / 2) - 100
root.geometry(f"300x200+{x}+{y}")

# 主窗口内容
zynr = "小猫头鹰在这里随意碎碎念，欢迎点击下面的按钮进行搜索或者退出！"
tk.Label(root, font=font.Font(size=16, weight='bold'), wraplength=280, text=zynr).pack(pady=10)

# 按钮设计
tk.Button(root, text="这就去搜索！", command=open_search_page, bg='lightblue', font=font.Font(size=12)).pack(pady=5)
tk.Button(root, text="还是算了吧！", command=close_main_window, bg='lightcoral', font=font.Font(size=12)).pack(pady=5)

# 状态信息标签
status_label = tk.Label(root, text="状态: 等待用户操作...", font=font.Font(size=12))
status_label.pack(pady=10)

love_bq = [
    "你今天过得怎么样？",
    "记得喝水哦！",
    "保持微笑，生活会更美好！",
    "小猫头鹰在为你加油！",
    "每天都是新的开始！",
    "你今天的目标是什么？",
    "休息一下，深呼吸！",
    "生活中的小确幸，常常被忽略！",
    "相信你自己，可以做到的！",
    "生活就是一场美丽的冒险！"
]

yoowl()  # 创建随机颜色窗口

root.mainloop()
