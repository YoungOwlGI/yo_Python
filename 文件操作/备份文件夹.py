import os
import stat
import time
import shutil


# 获取文件详细信息（类似于 `ls -al`）
def get_file_info(file_path):
    try:
        file_stat = os.stat(file_path)
        permissions = stat.filemode(file_stat.st_mode)
        file_size = file_stat.st_size
        modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_stat.st_mtime))
        return f"{permissions} {file_size} {modified_time} {file_path}"
    except Exception as e:
        return f"无法获取文件信息: {file_path}, 错误: {e}"


# 备份文件夹
def backup_directory(folder_path, backup_folder_path):
    try:
        folder_name = os.path.basename(folder_path.rstrip(os.sep))
        backup_folder_name = f"{folder_name}"
        full_backup_path = os.path.join(backup_folder_path, backup_folder_name)
        shutil.copytree(folder_path, full_backup_path)
        print(f"文件夹备份成功，备份路径: {full_backup_path}")
    except Exception as e:
        print(f"备份失败: {e}")


# 生成类似 `ls -al` 的文件详细信息列表
def save_file_info_list(folder_path, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(f"正在扫描文件夹 {folder_path}...\n")
            for root, dirs, files in os.walk(folder_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    file_info = get_file_info(file_path)
                    file.write(file_info + "\n")
        print(f"文件详细信息已保存至: {output_path}")
    except Exception as e:
        print(f"保存文件详细信息失败: {e}")


# 生成类似 `ls -R` 的递归文件夹结构
def save_recursive_file_list(folder_path, output_path):
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            for root, dirs, files in os.walk(folder_path):
                file.write(f"{root}:\n")
                for name in files:
                    file.write(f"  {name}\n")
                for name in dirs:
                    file.write(f"  {name}/\n")
                file.write("\n")
        print(f"递归文件夹结构已保存至: {output_path}")
    except Exception as e:
        print(f"保存递归文件夹结构失败: {e}")


# 主函数
def main():
    while True:
        print("\n请选择要执行的功能：")
        print("1. 备份文件夹")
        print("2. 生成文件详细信息列表（类似 ls -al）")
        print("3. 生成递归文件夹结构（类似 ls -R）")
        print("4. 退出程序")

        choice = input("请输入选择（1-4）：").strip()

        if choice == "1":
            folder_path = input("请输入需要备份的文件夹路径：").strip()
            backup_folder_path = input("请输入备份文件夹的目标路径：").strip()
            backup_directory(folder_path, backup_folder_path)
        elif choice == "2":
            folder_path = input("请输入需要扫描的文件夹路径：").strip()
            output_path = os.path.join(os.path.dirname(folder_path), os.path.basename(folder_path) + "_file_info.txt")
            save_file_info_list(folder_path, output_path)
        elif choice == "3":
            folder_path = input("请输入需要扫描的文件夹路径：").strip()
            output_path = os.path.join(os.path.dirname(folder_path),
                                       os.path.basename(folder_path) + "_recursive_list.txt")
            save_recursive_file_list(folder_path, output_path)
        elif choice == "4":
            print("程序已退出，再见！")
            break
        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
