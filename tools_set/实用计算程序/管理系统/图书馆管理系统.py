books = [
    ("崩坏3原画集·海与星的彼岸","崩坏3项目组","2024")
    ("Python程序设计与数据采集","董付国","2023")
         ]

def add_book():
    title = input("请输入书名：")
    author = input("请输入作者：")
    year = int(input("请输入出版年份："))
    books.append((title, author, year))
    print(f"图书 {title} 已添加！")

def show_book():
    if len(books) == 0:
        print("图书馆暂无图书！")
    else:
        print("图书列表：")
        for book in books:
            print(f"书名：{book[0]}, 作者：{book[1]}, 出版年份：{book[2]}")

def revise_book():
    if len(books) == 0:
        print("图书馆暂无图书！")
    else:
        title = input("请输入要修改的书名：")
        for i in range(len(books)):
            if books[i][0] == title:
                new_title = input("请输入新的书名：")
                new_author = input("请输入新的作者：")
                new_year = int(input("请输入新的出版年份："))
                books[i] = (new_title, new_author, new_year)  # 更新列表中的元组
                print(f"图书 {title} 的信息已修改为：{new_title}，{new_author}，{new_year}！")
                break
        else:
            print(f"图书 {title} 不存在！")

def delete_book():
    if len(books) == 0:
        print("图书馆暂无图书！")
    else:
        title = input("请输入要删除的书名：")
        for i in range(len(books)):
            if books[i][0] == title:  # 使用索引访问元组
                del books[i]
                print(f"图书 {title} 已删除！")
                break
        else:
            print(f"图书 {title} 不存在！")

def search_book():
    if len(books) == 0:
        print("图书馆暂无图书！")
    else:
        title = input("请输入要搜索的书名：")
        for book in books:
            if book[0] == title:
                print(f"书名：{book[0]}, 作者：{book[1]}, 出版年份：{book[2]}")
                break
        else:
            print(f"图书 {title} 不存在！")

while True:
    print("""
        欢迎使用图书馆管理系统！
        1. 添加图书
        2. 显示图书列表
        3. 修改图书信息
        4. 删除图书
        5. 搜索图书
        6. 退出
    """)
    choice = int(input("请输入你的选择："))
    if choice == 1:
        add_book()
    elif choice == 2:
        show_book()
    elif choice == 3:
        revise_book()
    elif choice == 4:
        delete_book()
    elif choice == 5:
        search_book()
    elif choice == 6:
        print("系统已退出，感谢使用！")
        break
    else:
        print("输入错误，请重新输入！")


"""
# 老师的方案

# 初始化图书列表
books = []
while True:
（此处做了处理）
    # print(‘’‘
    # 欢迎使用图书管理系统！
    # 1. 添加图书
    # 2. 显示图书列表
    # 3. 修改图书信息
    # 4. 删除图书
    # 5. 搜索图书
    # 6. 退出
    # ’‘’)
（处理直至此处）
    choice = input("请输入你的选择：")
    if choice == '1':
        # 添加图书
        title = input("请输入书名：")
        author = input("请输入作者：")
        year = int(input("请输入出版年份："))
        # 使用元组存储图书信息
        book = (title, author, year)
        books.append(book)
        print("图书已添加！")
    elif choice == '2':
        # 显示图书列表
        if len(books) == 0:
            print("当前图书列表为空！")
        else:
            print("当前图书列表：")
            for i, book in enumerate(books, 1):
                print(f"{i}. 《{book[0]}》 - {book[1]} - {book[2]}")
    elif choice == '3':
        # 修改图书信息
        if len(books) == 0:
            print("当前图书列表为空，无法修改！")
        else:
            book_number = int(input("请输入要修改的图书编号：")) - 1
            if 0 <= book_number < len(books):
                title = input("请输入新的书名：")
                author = input("请输入新的作者：")
                year = int(input("请输入新的出版年份："))
                books[book_number] = (title, author, year)
                print("图书信息已修改！")
            else:
                print("输入的图书编号无效！")
    elif choice == '4':
        # 删除图书
        if len(books) == 0:
            print("当前图书列表为空，无法删除！")
        else:
            book_number = int(input("请输入要删除的图书编号：")) - 1
            if 0 <= book_number < len(books):
                deleted_book = books.pop(book_number)
                print(f"图书《{deleted_book[0]}》已删除！")
            else:
                print("输入的图书编号无效！")
    elif choice == '5':
        # 搜索图书
        search_title = input("请输入要搜索的书名：")
        found = False
        for book in books:
            if book[0] == search_title:
                print(f"找到图书：《{book[0]}》 - {book[1]} - {book[2]}")
                found = True
                break
        if not found:
            print(f"未找到书名为《{search_title}》的图书！")
    elif choice == '6':
        # 退出系统
        print("系统已退出，感谢使用！")
        break
    else:
        print("无效输入，请重新选择！")
"""