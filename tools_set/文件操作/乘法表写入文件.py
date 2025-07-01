# 打开一个文件用于写入
with open('multiplication_table.txt', 'w') as file:
    for x in range(1, 1936):
        for y in range(1, x + 1):
            # 将乘法表达式和结果写入文件，而不是打印到控制台
            file.write(f"{y} * {x} = {x * y}\t")
        # 换行，开始下一行的乘法表达式
        file.write("\n")
