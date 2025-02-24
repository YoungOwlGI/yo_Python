import os
import random

def generate_random_content(index):
    # 可以根据索引或随机数生成不同的内容
    return f'这是第 {index} 个文档的内容，随机数是 {random.randint(1, 100)}。\n'

def create_files(num_files):
    for i in range(1, num_files + 1):
        file_name = f'docu11ment_{i}.txt'
        with open(file_name, 'w', encoding='utf-8') as file:
            content = generate_random_content(i)
            file.write(content)
            file.write('这里是一些示例文本。\n')
        print(f'已生成: {file_name}')

# 设置要生成的文档数量
num_files_to_create = 502
create_files(num_files_to_create)
