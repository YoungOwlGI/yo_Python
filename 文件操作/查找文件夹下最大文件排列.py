# 有误


import os


def find_large_files(path, size_limit):
    """
    查找指定路径下大于指定大小的文件，并返回文件路径和大小的字典。

    参数:
        path (str): 搜索的路径。
        size_limit (int): 文件大小限制，单位为字节。

    返回:
        dict: 包含文件路径和大小的字典，键为文件路径，值为文件大小。
    """
    large_files = {}

    # 检查路径是否有效
    if not os.path.exists(path):
        print(f"路径 '{path}' 不存在.")
        return large_files

    # 检查大小限制是否为正数
    if size_limit <= 0:
        print("大小限制必须为正数.")
        return large_files

    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                # 获取文件大小
                try:
                    file_size = os.path.getsize(file_path)
                    # 判断文件大小是否大于指定大小，如果是则添加到字典中
                    if file_size > size_limit:
                        large_files[file_path] = file_size
                        print(f'{file_path}: {file_size / (1024 * 1024):.2f} MB')
                except PermissionError:
                    print(f"没有权限访问文件 '{file_path}'.")
                except Exception as e:
                    print(f"在获取文件大小时出错: {e}")
                    # 根据文件大小降序排列
        large_files = {k: v for k, v in sorted(large_files.items(), key=lambda x: x[1], reverse=True)}
    except Exception as e:
        print(f"在查找大文件时出错: {e}")

    return large_files


def main():
    # 指定路径
    root = r"C:/"
    # 查找大于50MB的文件，并按照获取的文件大小降序排列打印结果
    # 50 * 1024 * 1024 ==> 50 M
    found_files = find_large_files(root, 500 * 1024 * 1024)
    if found_files:
        print("*" * 500)
        print("对以上结果根据文件大小降序排列:")
        for file, size in found_files:
            print(f'{file}: {size / (1024 * 1024):.2f} MB')
    else:
        print("没有找到大于50MB的文件.")


if __name__ == '__main__':
    main()
