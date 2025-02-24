# 输入字符串
input_text = """
李诗琪 信息学院 23级计算机应用技术6班23级信息学院计算级应用技术6班时建南23信息学院计算级应用技术6班时建南信息学院23级计算机应用技术6班时建南
"""

# 以“班”为分隔符，将字符串分割成列表
lines = input_text.strip().split('班')

# 在每个分割后的字符串后面加上“班”，并去除多余的空格
formatted_lines = [line.strip() + '班' for line in lines if line.strip()]

# 打印结果
for line in formatted_lines:
    print(line)