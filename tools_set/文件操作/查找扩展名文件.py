import glob
import os


def find_files_with_extension(directory, extension):
    # 使用glob的递归搜索功能
    # '**' 表示任何目录，'*.extension' 表示具有指定扩展名的文件
    for filepath in glob.iglob(os.path.join(directory, '**', '*.' + extension), recursive=True):
        print(filepath)

    # 替换为你想要搜索的目录和扩展名


directory = r"D:\猫头鹰的文件\计算机专题"  # 例如："/home/user/Documents"
extension = input("请输入扩展名：")

find_files_with_extension(directory, extension)
