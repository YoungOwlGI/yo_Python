import tkinter as tk
from tkinter import messagebox
import sqlite3


class LibrarySystem:
    def __init__(self, master):
        self.master = master
        master.title("图书馆管理系统")
        master.geometry("500x450")
        master.resizable(0, 0)

        # 定义变量
        self.book_id = tk.StringVar()
        self.book_name = tk.StringVar()
        self.book_author = tk.StringVar()
        self.book_publisher = tk.StringVar()
        self.book_price = tk.StringVar()
        self.book_num = tk.StringVar()
        self.borrow_num = tk.StringVar()
        self.borrow_id = tk.StringVar()
        self.borrow_name = tk.StringVar()
        self.borrow_time = tk.StringVar()
        self.borrow_return_time = tk.StringVar()

        # 定义函数
        def add_book():
            book_id = self.book_id.get()
            book_name = self.book_name.get()
            book_author = self.book_author.get()
            book_publisher = self.book_publisher.get()
            book_price = self.book_price.get()
            book_num = self.book_num.get()
            conn = sqlite3.connect("library.db")
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO books (book_id, book_name, book_author, book_publisher, book_price, book_num) VALUES (?, ?, ?, ?, ?, ?)",
                    (book_id, book_name, book_author, book_publisher, book_price, book_num))
                conn.commit()
                messagebox.showinfo("提示", "图书添加成功！")
            except sqlite3.Error as e:
                messagebox.showerror("错误", f"数据库错误: {e}")
            finally:
                conn.close()

        # 其他函数：delete_book, update_book, search_book, borrow_book, return_book ...

        # 定义标签和输入框
        tk.Label(master, text="图书ID：").place(x=10, y=10)
        tk.Entry(master, textvariable=self.book_id).place(x=100, y=10)

        tk.Label(master, text="图书名称：").place(x=10, y=40)
        tk.Entry(master, textvariable=self.book_name).place(x=100, y=40)

        # 更多标签和输入框...

        # 定义按钮
        tk.Button(master, text="添加图书", command=add_book).place(x=10, y=350)
        # 更多按钮定义...


if __name__ == '__main__':
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()
