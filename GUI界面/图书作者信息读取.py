import tkinter as tk

def display_info():
    work = entry_work.get()
    author = entry_author.get()
    text_info.delete('1.0', tk.END)
    text_info.insert(tk.END, f"作品: {work}\n作者: {author}")

app = tk.Tk()
app.title("Information Display")

tk.Label(app, text="作品").pack()
entry_work = tk.Entry(app)
entry_work.pack()

tk.Label(app, text="作者").pack()
entry_author = tk.Entry(app)
entry_author.pack()

button_read = tk.Button(app, text="读取信息", command=display_info)
button_read.pack()

text_info = tk.Text(app)
text_info.pack()

button_exit = tk.Button(app, text="退出", command=app.quit)
button_exit.pack()

app.mainloop()

