def main():
    while True:
        num_input = input("请输入当前值（输入q退出）：")
        # 检查是否输入了退出命令
        if num_input.lower() == 'q':
            print("程序结束。")
            break  # 使用break来退出循环

        # 尝试将输入转换为浮点数
        try:
            num = float(num_input)
            # 此处输入相关数值
            all_num = 17.9
            unit = "GB"
            # 次处即为输出
            print(
                " 当前已下载", num, unit, "\n",
                "还要下载", round(all_num - num, 2), unit, "\n",
                "共", all_num, unit, "\n",
                "进度：", round((num / all_num) * 100, 2), "%"
            )
        except ValueError:
            print("不合法输入，请输入一个数字或q来退出。")


if __name__ == "__main__":
    main()  # 直接调用main函数