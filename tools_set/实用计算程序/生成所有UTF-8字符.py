import unicodedata

# 创建或清空文件以输出所有 UTF-8 字符
with open("all_utf8_characters.txt", "w", encoding="utf-8") as f:
    for code_point in range(0x110000):  # Unicode 范围是 0x0000 到 0x10FFFF
        try:
            char = chr(code_point)  # 获取字符
            # 获取字符的名称（可选）
            name = unicodedata.name(char)
            f.write(f"{char}  # {name}\n")  # 写入字符和名称
        except (ValueError, UnicodeEncodeError):  # 不可打印的字符会引发错误
            continue

print("所有 UTF-8 字符已写入到 all_utf8_characters.txt 文件中。")
