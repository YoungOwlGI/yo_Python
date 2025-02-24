"""
    用处：
    将文件1内的文件的指定字符所{开头}的行 输出 到文件2内。
    格式：txt
"""

# 输入文件和输出文件的名称
input_file_name = 'list.txt'
output_file_name = 'output_1.txt'

# 打开输入文件进行读取，打开输出文件准备写入
num = input("请输入要保留的字符行\n请注意：\n1.不区分大小写。\n2.必须是行头。\n-->____")
with (open(input_file_name, 'r', encoding="utf-8") as input_file,
      open(output_file_name, 'w', encoding="utf-8") as output_file):
    # 逐行读取输入文件
    for line in input_file:
        # 检查当前行是否以"Name"开头（忽略大小写）
        if line.lower().startswith(num):
            # 将符合条件的行写入输出文件
            output_file.write(line)

# 打印完成消息
print(f"All lines starting with ‘{num}’ have been written to {output_file_name}")
