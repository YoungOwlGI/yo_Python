import tkinter as tk
from tkinter import ttk
from itertools import combinations

data = {
    "火": [15, 0, 0],
    "水": [13, 0, 0],
    "风": [11, 0, 0],
    "雷": [13, 0, 0],
    "草": [10, 0, 0],
    "冰": [15, 0, 0],
    "岩": [11, 0, 0]
}

# 更新日期
update_date = "新深渊——幻想真境剧诗 角色详情"

def calculate_achievement_rate(count1, count2):
    if count1 == 0:
        return 0.0
    return count2 / count1 * 100

def display_results():
    for element in data:
        data[element][1] = int(entries[element][0].get())
        data[element][2] = int(entries[element][1].get())

    result_text.delete(1.0, tk.END)
    index = 1
    for combo in combinations(data.keys(), 3):
        elements = list(combo)
        total_count_all = sum(data[element][0] for element in elements)
        total_count_mine = sum(data[element][1] for element in elements)
        total_count_satisfied = sum(data[element][2] for element in elements)
        achievement_rate_mine_all = calculate_achievement_rate(total_count_all, total_count_mine)
        achievement_rate_satisfied_mine = calculate_achievement_rate(total_count_mine, total_count_satisfied)
        result_text.insert('end', f"{index}. {'+'.join(elements)}: 已出角色总数 {total_count_all}, 我的角色总数 {total_count_mine}, 符合要求角色总数 {total_count_satisfied}, 我的角色占已出角色百分比 {achievement_rate_mine_all:.2f}%, 符合要求角色占我的角色百分比 {achievement_rate_satisfied_mine:.2f}%")
        result_text.insert('end', '\n')  # 确保在每个结果后插入换行符
        index += 1


# 创建主窗口
root = tk.Tk()
root.title("新深渊——幻想真境剧诗 角色详情")
root.geometry("900x700")

# 添加标签
title_label = tk.Label(root, text=f"程序：{update_date}", font=("Helvetica", 14))
title_label.pack(pady=10)

# 创建输入框
tk.Label(root, text="请输入每个元素的用户数据：\n(已出角色: 总数, 我的角色: 总数, 符合要求角色: 总数)", font=("Helvetica", 12)).pack(pady=5)
entries = {}
entry_frame = tk.Frame(root)
entry_frame.pack()

for element in data:
    frame = tk.Frame(entry_frame)
    frame.pack(pady=2, anchor="w")
    tk.Label(frame, text=f"{element} (已出角色: {data[element][0]}):", font=("Helvetica", 12)).pack(side="left")
    user_char_entry = tk.Entry(frame, width=5)
    user_char_entry.pack(side="left", padx=5)
    high_level_entry = tk.Entry(frame, width=5)
    high_level_entry.pack(side="left", padx=5)
    entries[element] = (user_char_entry, high_level_entry)

# 添加结果显示文本框
result_text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), height=20, width=100)
result_text.pack(padx=10, pady=10)

# 添加按钮
generate_button = ttk.Button(root, text="生成角色组合详情", command=display_results)
generate_button.pack(pady=5)

# 运行主循环
root.mainloop()
