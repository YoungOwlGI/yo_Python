"""
    作者：文心一言 小猫头鹰
    适用：扫描对应文件夹内的文件夹的大小（B、MB、GB三种大小）
    禁忌：直接扫描根目录（"C:\" 和 "D:\"）
"""

import os


def convert_size(size_bytes):
    """
    将字节大小转换为更易读的格式，包括字节、MB和GB。
    """
    if size_bytes == 0:
        return "0 Bytes | 0 MB | 0 GB"
    size_mb = size_bytes / (1024 ** 2)
    size_gb = size_mb / 1024
    return f"{size_bytes} Bytes | {size_mb:.2f} MB | {size_gb:.2f} GB"


def get_folder_size(folder):
    """
    返回文件夹的大小（字节）。
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def list_folder_sizes(root_folder, output_file):
    """
    列出root_folder下所有子文件夹的大小，并将结果写入到output_file指定的文件中。
    """
    with open(output_file, 'w') as f:
        for foldername in os.listdir(root_folder):
            folder_path = os.path.join(root_folder, foldername)
            if os.path.isdir(folder_path):
                size = get_folder_size(folder_path)
                converted_size = convert_size(size)
                output_line = f"{foldername}: {converted_size}\n"
                print(output_line, end='')  # 在控制台上打印
                f.write(output_line)  # 写入到文件中


# 使用示例
root_folder = r"D:\leidian\LDPlayer9\vms"  # 替换为您的文件夹路径
output_file = "output.txt"  # 指定输出文件的路径
list_folder_sizes(root_folder, output_file)
