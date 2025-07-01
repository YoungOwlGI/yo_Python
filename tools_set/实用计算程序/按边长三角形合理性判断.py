while True:
    try:
        a = int(input("请输入三角形的第一个边长："))
        b = int(input("请输入三角形的第二个边长："))
        c = int(input("请输入三角形的第三个边长："))

        if a + b > c and b + c > a and c + a > b:
            print("能构成三角形")
            break
        else:
            print("不能构成三角形，请重新输入")
    except ValueError:
        print("输入的不是数字")