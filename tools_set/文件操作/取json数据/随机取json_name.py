import random
import json

# 加载 JSON 文件
with open('D:/猫头鹰的文件/计算机专题/Python/文件操作/取json数据/index.json'
          , 'r', encoding='utf-8') as file:
    data = json.load(file)

# 确保 'files' 是一个列表，且包含至少一个实验文件
if 'files' in data and isinstance(data['files'], list):
    # 过滤出所有 `.ipynb` 文件
    notebooks = [file['name'] for file in data['files'] if file['name'].endswith('.png')]

    # 随机选择一个实验文件
    if notebooks:
        selected_notebook = random.choice(notebooks)
        print(f"随机选择的实验文件是: {selected_notebook}")
    else:
        print("没有找到任何 .png 文件")
else:
    print("文件结构不正确或没有可用的文件")