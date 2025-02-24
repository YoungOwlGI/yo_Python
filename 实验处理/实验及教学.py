import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("抽卡计算器")
root.geometry("300x400")

# 存储输入框和复选框的变量
input_vars = []
checkbox_vars = []

# 输入框1和复选框1
label1 = tk.Label(root, text="请输入原石数量：")
label1.grid(row=0, column=0, padx=10, pady=5, sticky='w')

input_var1 = tk.StringVar()
input_entry1 = tk.Entry(root, textvariable=input_var1, width=10)
input_entry1.grid(row=0, column=1, padx=10, pady=5)

checkbox_var1 = tk.BooleanVar()
input_checkbox1 = tk.Checkbutton(root, variable=checkbox_var1)
input_checkbox1.grid(row=0, column=2, padx=10, pady=5)

input_vars.append(input_var1)
checkbox_vars.append(checkbox_var1)

# 输入框2和复选框2
label2 = tk.Label(root, text="请输入纠缠之缘数量：")
label2.grid(row=1, column=0, padx=10, pady=5, sticky='w')

input_var2 = tk.StringVar()
input_entry2 = tk.Entry(root, textvariable=input_var2, width=10)
input_entry2.grid(row=1, column=1, padx=10, pady=5)

checkbox_var2 = tk.BooleanVar()
input_checkbox2 = tk.Checkbutton(root, variable=checkbox_var2)
input_checkbox2.grid(row=1, column=2, padx=10, pady=5)

input_vars.append(input_var2)
checkbox_vars.append(checkbox_var2)

# 输入框3和复选框3
label3 = tk.Label(root, text="请输入星辉数量：")
label3.grid(row=2, column=0, padx=10, pady=5, sticky='w')

input_var3 = tk.StringVar()
input_entry3 = tk.Entry(root, textvariable=input_var3, width=10)
input_entry3.grid(row=2, column=1, padx=10, pady=5)

checkbox_var3 = tk.BooleanVar()
input_checkbox3 = tk.Checkbutton(root, variable=checkbox_var3)
input_checkbox3.grid(row=2, column=2, padx=10, pady=5)

input_vars.append(input_var3)
checkbox_vars.append(checkbox_var3)

# 输入框4和复选框4
label4 = tk.Label(root, text="请输入垫的数量：")
label4.grid(row=3, column=0, padx=10, pady=5, sticky='w')

input_var4 = tk.StringVar()
input_entry4 = tk.Entry(root, textvariable=input_var4, width=10)
input_entry4.grid(row=3, column=1, padx=10, pady=5)

checkbox_var4 = tk.BooleanVar()
input_checkbox4 = tk.Checkbutton(root, variable=checkbox_var4)
input_checkbox4.grid(row=3, column=2, padx=10, pady=5)

input_vars.append(input_var4)
checkbox_vars.append(checkbox_var4)

# 输入框5和复选框5
label5 = tk.Label(root, text="请输入创世结晶数量：")
label5.grid(row=4, column=0, padx=10, pady=5, sticky='w')

input_var5 = tk.StringVar()
input_entry5 = tk.Entry(root, textvariable=input_var5, width=10)
input_entry5.grid(row=4, column=1, padx=10, pady=5)

checkbox_var5 = tk.BooleanVar()
input_checkbox5 = tk.Checkbutton(root, variable=checkbox_var5)
input_checkbox5.grid(row=4, column=2, padx=10, pady=5)

input_vars.append(input_var5)
checkbox_vars.append(checkbox_var5)

# 计算按钮
calculate_button = tk.Button(root, text="计算", command=lambda: calculate_sum(input_vars, checkbox_vars))
calculate_button.grid(row=5, column=0, columnspan=3, pady=20)

# 显示结果的标签
result_label = tk.Label(root, text="目前抽数: ")
result_label.grid(row=6, column=0, columnspan=3, pady=10)

def calculate_sum(input_vars, checkbox_vars):
    try:
        sum_value = 0
        for i in range(len(input_vars)):
            if checkbox_vars[i].get():
                sum_value += float(input_vars[i].get())
        result_label.config(text=f"目前抽数: {sum_value}")
    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字")

# 运行主循环
root.mainloop()
