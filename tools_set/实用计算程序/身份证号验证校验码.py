'''
    只运行一次
'''

# sfzh = input("请输入身份证号前十七位：")
#
# # 将字符串转换为整数列表
# sfzh_numbers = [int(num) for num in sfzh]
#
# # 根据权重计算求和
# weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
# suma = sum(a * b for a, b in zip(sfzh_numbers, weights))
#
# # 计算校验码
# zhi = suma % 11
#
# # 根据得到的余数确定校验码
# if zhi == 0:
#     check_digit = '1'
# elif zhi == 1:
#     check_digit = '0'
# elif zhi == 2:
#     check_digit = 'X'
# else:
#     check_digit = 12 - zhi
#
# print("身份证号的最后一位校验码是：", check_digit)

'''
    文心一言一代 函数 回答。
        含有微小改动
'''

# def calculate_check_digit(sfzh_numbers):
#     weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
#     suma = sum(a * b for a, b in zip(sfzh_numbers, weights))
#     zhi = suma % 11
#
#     # 根据得到的余数确定校验码
#     if zhi == 0:
#         return '1'
#     elif zhi == 1:
#         return '0'
#     elif zhi == 2:
#         return 'X'
#     else:
#         return str(12 - zhi)
#
#
# def main():
#     while True:
#         sfzh_input = input("请输入身份证号前十七位（或输入'quit'退出）：")
#         if sfzh_input.lower() == 'quit':
#             break
#         if len(sfzh_input) != 17 or not sfzh_input.isdigit():
#             print("输入不合法，请输入正确的17位数字身份证号！")
#             continue
#         sfzh_numbers = [int(num) for num in sfzh_input]
#         check_digit = calculate_check_digit(sfzh_numbers)
#         print("身份证号的最后一位校验码是：", check_digit)
#
#
# if __name__ == "__main__":
#     main()

'''
    叮！快来看看我和文心一言的奇妙对话～点击链接 https://yiyan.baidu.com/share/TQ7tcd4Bj9
        -- 文心一言，既能写文案、读文档，又能绘画聊天、写诗做表，你的全能伙伴！
            嘴犟的文心一言 之后给的结果。
'''


def calculate_check_digit(sfzh_numbers):
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = '10X98765432'
    suma = sum(a * b for a, b in zip(sfzh_numbers, weights))
    index = suma % 11
    return check_codes[index]


def main():
    while True:
        sfzh_input = input("请输入身份证号前十七位（或输入'quit'退出）：")
        if sfzh_input.lower() == 'quit':
            break
        if len(sfzh_input) != 17 or not sfzh_input.isdigit():
            print("输入不合法，请输入正确的17位身份证号数字部分！")
            continue
        sfzh_numbers = [int(num) for num in sfzh_input]
        check_digit = calculate_check_digit(sfzh_numbers)
        print("身份证号的最后一位校验码是：", check_digit)


if __name__ == "__main__":
    main()
