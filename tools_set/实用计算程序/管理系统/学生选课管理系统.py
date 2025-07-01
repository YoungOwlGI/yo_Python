courses = [
    {"name": "烟雾原理", "teacher": "西特拉莉", "credits": 3},
    {"name": "元素反应理论", "teacher": "阿贝多", "credits": 4},
    {"name": "雨林生态学", "teacher": "提纳里", "credits": 3},
    {"name": "遗迹考古学", "teacher": "珐露珊", "credits": 4},
    {"name": "军事理论", "teacher": "珊瑚宫心海", "credits": 3},
]

students = {}

def list_all_courses():
    print("==================所有可选课程：==================")
    for course in courses:
        print(f"【课程名称：{course['name']}】【授课教师：{course['teacher']}】【课程学分：{course['credits']}】")

def add_student(name, selected_courses):
    student = {"name": name, "courses": selected_courses}
    students[name] = student
    print("学生添加成功！")

def enroll_course():
    name = input("请输入学生姓名：")
    if name not in students:
        selected_courses = input("请输入已选课程（用逗号分隔）：").split(',')
        selected_courses = [course.strip() for course in selected_courses]  # 去除课程名称两端的空格
        add_student(name, selected_courses)
    else:
        print("该学生已存在，请选择不同的姓名。")

def drop_course():
    name = input("请输入学生姓名：")
    if name in students:
        course_to_drop = input("请输入要退选的课程名称：")
        if course_to_drop in students[name]["courses"]:
            students[name]["courses"].remove(course_to_drop)
            print(f"成功退选课程：{course_to_drop}")
        else:
            print("该课程不在学生已选课程中。")
    else:
        print("没有找到该学生。")

def query_student():
    name = input("请输入学生姓名：")
    student = students.get(name)
    if student:
        print("学生姓名：", student["name"])
        print("已选课程：", student["courses"])
    else:
        print("没有找到该学生")

def list_all_students():
    print("所有学生选课情况：")
    if students:  # 检查学生字典是否为空
        for name, student in students.items():
            print("学生姓名：", student["name"])
            print("已选课程：", student["courses"])
    else:
        print("当前没有任何学生信息。")

def main():
    print("欢迎使用选课系统")
    menu = {
        "1": list_all_courses,
        "2": enroll_course,
        "3": drop_course,
        "4": query_student,
        "5": list_all_students,
        "6": exit_system
    }

    while True:
        print("\n1. 查看可选课程")
        print("2. 选择课程")
        print("3. 退选课程")
        print("4. 查看已选课程")
        print("5. 查看所有学生选课情况")
        print("6. 退出系统")

        choice = input("请输入您的选择：")
        action = menu.get(choice)
        if action:
            action()  # 调用相应的函数
        else:
            print("输入错误，请重新输入")

def exit_system():
    print("谢谢使用选课系统，再见！")
    exit()

if __name__ == "__main__":
    main()