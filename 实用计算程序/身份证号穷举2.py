import random
import os
"""
# 获取日期列表mmdd格式
mmdd = []
for m in range(1, 13):
    for d in range(1, 32):
        mmdd.append('%02d%02d' % (m, d))
temp = ['0229', '0230', '0231', '0431', '0631', '0931', '1131']
for i in temp:
    mmdd.remove(i)

# 身份证号码验证
def id_check(ID):
    # ID值为str
    if len(ID) != 18:
        print('输入错误的身份证号码')
    else:
        id_code = ID[17]  # 校验码
        q = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        id_num = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        total = 0
        for i in range(len(q)):
            total = total + (int(ID[i]) * q[i])
        id_mod = total % 11
        if id_num[id_mod] == id_code:
            print('该身份证号码已验证：' + ID)
            # return ID
        # else:
        #     print('该身份证号码错误，正确为：', (ID[:-1] + id_num[id_mod]))  # 错误的输出正确号码

def main(id):
    id_year = int(id.split('****')[0][-4:])  # 身份证年份
    mmdd_1 = mmdd[:]
    if (id_year % 4):  # 判断闰年，因1900年出生的人没有身份证号，故不做考虑
        pass
    else:
        mmdd_1.append('0229')
    for i in mmdd_1:
        ID = id.replace('****',i)
        id_check(ID)

if __name__ == '__main__':
    id = '5104021998****0110'
    # id_check('510402199812240110')  # 验证单个号码是否正确
    main(id)
"""

def calculate_checksum(id_number_base):
    # 身份证号的校验码计算规则
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checksum_map = "10X98765432"
    sum_ = sum(int(id_number_base[i]) * weights[i] for i in range(17))
    return checksum_map[sum_ % 11]


def generate_id_numbers(prefix14, output_file):
    # 确保前14位是合法的
    if len(prefix14) != 14 or not prefix14.isdigit():
        raise ValueError("前14位必须是14位数字")

    # 奇数的第17位选项
    odd_digits = "13579"

    with open(output_file, 'w') as file:
        for _ in range(10000):  # 穷举第15和16位的10000种可能
            # 随机生成第15和16位
            random_two_digits = f"{random.randint(0, 99):02d}"

            for odd_digit in odd_digits:
                # 组合成前17位
                prefix17 = prefix14 + random_two_digits + odd_digit

                # 计算第18位的校验码
                checksum = calculate_checksum(prefix17)

                # 生成完整的18位身份证号
                id_number = prefix17 + checksum

                # 将结果写入文件
                file.write(id_number + '\n')


# 输入前14位的身份证号
prefix14 = "41150220050612"  # 示例前14位
output_file = "id_numbers.txt"  # 输出文件名

# 生成身份证号并写入文件
generate_id_numbers(prefix14, output_file)

print(f"身份证号已生成并写入文件: {output_file}")
