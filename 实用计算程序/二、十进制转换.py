# 十转二
def ten_two():
    original_decimal_num = int(input("请输入要转换为二进制的十进制数："))
    decimal_num = original_decimal_num
    binary_num = ''
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2
    print("{}的二进制的表示是:{}".format(original_decimal_num, binary_num))


# 二转十
def two_ten():
    binary_str = input("请输入要转换为十进制的二进制数（只包含0和1）：")
    decimal_num = 0
    # 反转二进制字符串，因为我们从最低位（最右边）开始计算
    binary_str = binary_str[::-1]
    # 遍历每一位，计算对应的十进制值
    for i, digit in enumerate(binary_str):
        decimal_num += int(digit) * 2 ** i
    print("{}的十进制表示是:{}".format(binary_str, decimal_num))


shuru = input("请选择转换形式（  ）：\nA：二进制转十进制\nB:十进制转二进制\n请输入选项：")
if shuru == "A":
    ten_two()
elif shuru == "B":
    two_ten()
else:
    print("请按照规则输入！")
