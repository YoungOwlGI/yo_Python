def remove_duplicates(input_file, output_file):
    # 用于存储唯一的行
    seen_lines = set()

    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                # 去掉行末的换行符
                line = line.strip()
                # 如果该行不在seen_lines集合中，则写入文件
                if line not in seen_lines:
                    outfile.write(line + '\n')
                    seen_lines.add(line)

# 输入文件名和输出文件名
input_file = 'id_numbers.txt'  # 输入文件名
output_file = 'unique_id_numbers.txt'  # 输出文件名

# 执行去重操作
remove_duplicates(input_file, output_file)

print(f"去重后的内容已写入文件: {output_file}")
