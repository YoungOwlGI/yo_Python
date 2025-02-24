students = {
    "小猫头鹰": 99,
    "YoungOwl": 98,
    "Catherine Erin": 97
}

def main():
    """
    主菜单函数，打印系统的功能选项。
    """
    print("1. 注册学生")
    print("2. 注销学生")
    print("3. 查询学生")
    print("4. 计算成绩")
    print("5. 退出系统")

def register():
    print("请选择注册方式：")
    if input("是否一次性输入学生姓名和成绩？（y/n）") == 'y':
        single_register()
    else:
        batch_register()

def single_register():
    name = input("请输入学生姓名（输入“end”退出）：")
    if name == "end":
        return
    score = int(input(f"请输入{name}的成绩："))
    students[name] = score
    print(f"学生 {name} 注册成功！")

def batch_register():
    while True:
        names = input("请输入学生姓名（多个姓名用逗号分隔，输入 'end' 结束，建议一次输入 5个学生）：")
        # 从用户获取输入的学生姓名，多个姓名用逗号分隔，'end'表示结束输入
        if names == 'end':
            break
        # 如果用户输入的是'end'，则跳出循环
        name_list = [name.strip() for name in names.split(',')]
        # 将用户输入的学生姓名字符串按逗号分割，然后去除每个姓名的前后空格，得到学生姓名列表
        grades_str = input("请输入对应的学生成绩（多个成绩用逗号分隔）：")
        # 从用户获取输入的与学生对应的成绩，多个成绩用逗号分隔
        grade_list = [int(grade.strip()) if grade.strip().isdigit() else None for grade in grades_str.split(',')]
        # 将用户输入的成绩字符串按逗号分割，然后去除每个成绩的前后空格，如果是数字则转换为整数，否则为 None，得到成绩列表
        if len(name_list) != len(grade_list):
            print("输入的学生姓名和成绩数量不匹配，请重新输入。")
            continue
        # 如果学生姓名列表和成绩列表的长度不相等，提示用户输入不匹配并继续下一次循环
        for name, grade in zip(name_list, grade_list):
            # 同时遍历学生姓名列表和成绩列表
            if name in students:
                print(f"学生 {name} 已注册！")
            # 如果学生姓名已经在学生字典中，说明该学生已注册，输出提示信息
            elif grade is None or grade < 1 or grade > 100:
                print(f"成绩输入错误，成绩应在 1 - 100 之间。")
            # 如果成绩为 None 或者不在 1 - 100 的范围内，提示用户成绩输入错误
            else:
                students[name] = grade
                print(f"学生 {name} 注册成功！")
        # 如果学生未注册且成绩输入正确，将学生姓名和成绩添加到学生字典中，并输出注册成功的提示信息

def unregister():
    """
    学生注销函数，根据用户输入的学生姓名进行注销操作。
    """
    name = input("请输入学生姓名：")
    if name in students:
        del students[name]
        print("注销成功！")
    else:
        print("该学生未注册！")

def query():
    """
    学生查询函数，根据用户输入的学生姓名查询其成绩。
    """
    name = input("请输入学生姓名：")
    if name in students:
        print("该学生的成绩为：", students[name])
    else:
        print("没有该学生的记录，现有学生分别是：")
        for name in students:
            print(name, end=' ╰(*°▽°*)╯ ')
        print("\n")

def traverse():
    total_grade = 0
    # 初始化总成绩为 0
    """
    下面这段代码的逻辑是为了在后续的处理中能够正确地找到学生成绩中的最大值和最小值。

        1. max_grade = float('-inf')
           - 将变量 `max_grade` 初始化为负无穷大。
           这样做的目的是确保在遍历学生成绩时，第一个遇到的成绩一定会比负无穷大更大，
           从而可以正确地更新 `max_grade` 为第一个成绩值，并且在后续的遍历中，
           如果遇到更大的成绩，就不断更新 `max_grade`。
        
        2. min_grade = float('inf')
           - 将变量 `min_grade` 初始化为正无穷大。
           同理，在遍历学生成绩时，第一个遇到的成绩一定会比正无穷小更小，
           这样可以正确地更新 `min_grade` 为第一个成绩值，并且在后续遍历中，
           如果遇到更小的成绩，就不断更新 `min_grade`。
    
    通过这种方式，可以在不知道学生成绩具体范围的情况下，有效地找到所有学生成绩中的最大值和最小值。
    """
    max_grade = float('-inf')
    # 初始化最高成绩为负无穷大
    min_grade = float('inf')
    # 初始化最低成绩为正无穷大
    num_students = len(students)
    # 获取学生总数
    num_passed_students = 0
    # 初始化及格学生数量为 0
    max_student_name = None
    # 初始化最高成绩学生的姓名为 None
    min_student_name = None
    # 初始化最低成绩学生的姓名为 None

    for student_name, student_grade in students.items():
        # 遍历学生字典，其中键为学生姓名，值为学生成绩
        total_grade += student_grade
        # 累加每个学生的成绩到总成绩
        if student_grade > max_grade:
            max_grade = student_grade
            max_student_name = student_name
        # 如果当前学生成绩高于最高成绩，则更新最高成绩和对应的学生姓名
        if student_grade < min_grade:
            min_grade = student_grade
            min_student_name = student_name
        # 如果当前学生成绩低于最低成绩，则更新最低成绩和对应的学生姓名
        if student_grade >= 60:
            num_passed_students += 1
        # 如果学生成绩大于等于 60，及格学生数量加一

    average = total_grade / num_students
    # 计算平均成绩，即总成绩除以学生总数
    print(f"所有学生的平均成绩为：, {average:.2f}")
    print("所有学生的最高成绩为：", max_grade)
    print("该学生的姓名是：", max_student_name)
    print("所有学生的最低成绩为：", min_grade)
    print("该学生的姓名是：", min_student_name)
    pass_rate = num_passed_students / num_students
    # 计算及格率，即及格学生数量除以学生总数
    print(f"所有学生的及格率为：, {pass_rate:.2%}")

while True:
    main()
    choice = input("请输入选项：")
    if choice == "1":
        register()
    elif choice == "2":
        unregister()
    elif choice == "3":
        query()
    elif choice == "4":
        traverse()
    elif choice == "5":
        print("欢迎下次使用！")
        break
    else:
        print("输入错误！")