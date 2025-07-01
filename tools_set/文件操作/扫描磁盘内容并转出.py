import os

# 替换为要扫描的文件夹路径，注意路径字符串中的双反斜杠或前置'r'表示原始字符串  
folder_path = r"D:"
output_file = os.path.join(folder_path, "file_list.txt")  # 使用os.path.join来构建文件路径  

with open(output_file, "w", encoding='utf-8') as file:  # 添加encoding参数以支持中文  
    file.write("正在扫描文件夹 " + folder_path + " 及其子文件夹内的文件...\n")
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file.write(file_path + "\n")

print("文件扫描完成！文件列表已保存到 " + output_file)
