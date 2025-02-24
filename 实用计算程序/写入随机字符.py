import random

def random_utf8_char():
    # 随机选择 Unicode 范围
    # 例如：这里选择了汉字 (U+4E00 到 U+9FA5)
    unicode_range = (0x4E00, 0x9FA5)  # 汉字范围
    random_code_point = random.randint(unicode_range[0], unicode_range[1])
    return chr(random_code_point)

# 写入随机字符和 i
with open("txt3.txt", "w", encoding="utf-8") as f:  # 使用 'w' 模式以清空文件
    for i in range(1, 1122):  # 从 0 到 1120
        random_char = random_utf8_char()  # 生成随机字符
        f.write(f"{random_char}\n")  # 写入随机字符和当前的 i 值

