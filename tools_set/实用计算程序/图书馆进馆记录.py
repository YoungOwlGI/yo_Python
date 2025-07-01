in_right = 0
out_lift = 0
while True:
    abc = input("a是右（正确）\nz是左（错误）\n请输入选项：")
    if abc == "a":
        in_right += 1
        print("当前从入口进入人数共",in_right , "人，从出口进入人数共", out_lift, "人。")
    elif abc == "z":
        out_lift += 1
        print("当前从入口进入人数共", in_right, "人，从出口进入人数共", out_lift, "人。")
    elif abc =="q":
        print("从入口进入人数共", in_right, "人，从出口进入人数共", out_lift, "人。")
        break
    else:
        print("请按规则输入！")
        continue



























































































data = {

    }