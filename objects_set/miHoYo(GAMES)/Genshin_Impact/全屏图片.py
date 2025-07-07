from PIL import Image, ImageTk
import tkinter as tk


def show_fullscreen_image(image_path):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.overrideredirect(True)

    img = Image.open(image_path)
    # 获取屏幕分辨率
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 调整图片尺寸以适应屏幕
    img = img.resize((screen_width, screen_height))
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=tk_img)
    label.pack()

    root.mainloop()

if __name__ == '__main__':
    show_fullscreen_image('./img/begin_2.png')