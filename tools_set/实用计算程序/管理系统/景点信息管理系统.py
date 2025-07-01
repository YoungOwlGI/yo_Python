name = [
    "故宫博物院","天坛","颐和园","长城","雕塑公园",
    "河南博物院","北京故宫","南京博物院","上海博物馆","苏州博物馆"
    ]

def add():
    print("请添加景点：")
    place = input()
    name.append(place)
    print("已添加：", place)

def show():
    print("所有景点：")
    for i in range(len(name)):
        print(i+1,"：", name[i])

def modify():
    show()
    index = int(input("请选择要修改的景点的序号："))
    print("请输入新的名称：")
    new_name = input("请输入新的名称：")
    name[index-1] = new_name
    print("已修改：", name[index-1])

def delete():
    show()
    index = int(input("请选择要删除的景点序号："))
    del name[index-1]
    print("已删除：", name[index-1])

def search():
    place = input("请输入要搜索的景点：")
    if place in name:
        print("已找到：", place)
    else:
        print("未找到：", place)
        show()

while True:
    print("1. 添加景点")
    print("2. 显示所有景点")
    print("3. 修改景点")
    print("4. 删除景点")
    print("5. 搜索景点")
    print("6. 退出程序")
    choice = int(input("请输入你的选择："))
    if choice == 1:
        add()
    elif choice == 2:
        show()
    elif choice == 3:
        modify()
    elif choice == 4:
        delete()
    elif choice == 5:
        search()
    elif choice == 6:
        exit()
    else:
        print("输入错误，请重新输入！")

