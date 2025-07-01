account_number = 0
print("欢迎使用银行账户管理系统！")

def deposit(amount):
    global account_number
    if amount > 0:  # 应该是大于0
        account_number += amount
        print("存款成功！当前账户余额为：", account_number)
    else:
        print("存款金额必须大于0！")

def withdraw(amount):
    global account_number
    if account_number < amount:
        print("余额不足！")
    else:
        account_number -= amount
        print("取款成功！当前账户余额为：", account_number)

def check_balance():
    global account_number
    print("当前账户余额为：", account_number)

def main():
    global account_number
    while True:
        print("1. 存款")
        print("2. 取款")
        print("3. 查询余额")
        print("4. 退出")
        choice = input("请输入您的选择：")
        if choice == "1":
            amount = int(input("请输入存款金额："))
            deposit(amount)
        elif choice == "2":
            amount = int(input("请输入取款金额："))
            withdraw(amount)
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("退出系统！感谢您的使用！")
            break
        else:
            print("输入错误！")

if __name__ == '__main__':
    main()
