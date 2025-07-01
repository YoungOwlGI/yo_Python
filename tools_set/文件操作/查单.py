import os
import hashlib


def calculate_md5(file_path):
    """计算文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_unique_files(folder1, folder2):
    """查找两个文件夹中的不重复文件"""
    files_hash = {}  # 存储文件夹1中文件的哈希值和路径
    unique_files = []  # 存储只在文件夹2中存在的文件

    # 遍历第一个文件夹，记录所有文件的哈希值
    for root, _, files in os.walk(folder1):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            files_hash[file_hash] = file_path

            # 遍历第二个文件夹，检查文件是否在文件夹1中存在
    for root, _, files in os.walk(folder2):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            if file_hash not in files_hash:
                unique_files.append(file_path)

    return unique_files


def main():
    try:
        folder1 = input("请输入第一个文件夹的路径: ")
        folder2 = input("请输入第二个文件夹的路径: ")
        unique_files_in_folder2 = find_unique_files(folder1, folder2)
        if unique_files_in_folder2:
            print("以下文件只在第二个文件夹中存在：")
            for file_path in unique_files_in_folder2:
                print(file_path)
        else:
            print("第二个文件夹中的所有文件在第一个文件夹中都存在。")
    except Exception as e:
        print("发生错误：", e)


if __name__ == "__main__":
    main()