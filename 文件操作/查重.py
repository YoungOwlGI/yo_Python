import os
import hashlib


def calculate_md5(file_path):
    """计算文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_duplicate_files(folder1, folder2):
    """查找两个文件夹中的重复文件"""
    files_hash = {}  # 用于存储文件的哈希值和路径
    duplicates = {}  # 用于存储重复的文件

    # 遍历第一个文件夹
    for root, _, files in os.walk(folder1):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            if file_hash in files_hash:
                if file_hash not in duplicates:
                    duplicates[file_hash] = [files_hash[file_hash]]
                duplicates[file_hash].append(file_path)
            else:
                files_hash[file_hash] = file_path

                # 遍历第二个文件夹
    for root, _, files in os.walk(folder2):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            if file_hash in files_hash:
                if file_hash not in duplicates:
                    duplicates[file_hash] = [files_hash[file_hash]]
                duplicates[file_hash].append(file_path)
            else:
                files_hash[file_hash] = file_path

    return duplicates


def main():
    try:
        folder1 = input("请输入第一个文件夹的路径: ")
        folder2 = input("请输入第二个文件夹的路径: ")
        duplicates = find_duplicate_files(folder1, folder2)
        if duplicates:
            print("找到以下重复文件：")
            for file_hash, paths in duplicates.items():
                print(f"哈希值: {file_hash}")
                for path in paths:
                    print(f"  {path}")
                print()
        else:
            print("未找到重复文件。")
    except Exception as e:
        print(f"错误：{e}")


if __name__ == "__main__":
    main()