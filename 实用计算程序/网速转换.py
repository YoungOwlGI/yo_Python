def main():
    while True:
        user_input = input("请输入目前数值（输入quit退出）：")
        if user_input.lower() == 'quit':
            break

        try:
            num = float(user_input)
            b = input("请输入单位（必须是MB或者mbps，也可以以A或者B代替。）：").upper()
            if b == "MB" or b == "A":
                print(num * 8, "mbps")
            elif b == "mbps" or b == "B":
                print(num / 8, "MB/s")
            else:
                print("单位不合法！")
        except ValueError:
            print("请输入有效的数值！")


if __name__ == "__main__":
    main()
