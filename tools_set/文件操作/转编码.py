# 打开原始文件，假设它是用其他编码（如GBK, ASCII等）保存的
with open('202.CSV', 'r', encoding='ANSI') as f:
    content = f.read()

# 将内容写入到新文件，使用UTF-8编码
with open('202.CSV', 'w', encoding='utf-8') as f:
    f.write(content)