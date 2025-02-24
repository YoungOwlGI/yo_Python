import json


# 读取 JSON 文件
def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"JSON 解码错误: {e}")
        return None
    except FileNotFoundError:
        print("未找到文件，请检查文件路径。")
        return None


# 根据名称查找文件属性
def find_file_by_name(data, name):
    for file in data['files']:
        if file['name'] == name:
            return file
    return None


def main():
    # 指定 JSON 文件路径
    json_file_path = 'D:/猫头鹰的文件/计算机专题/Python/文件操作/取json数据/index.json'

    # 加载 JSON 数据
    data = load_json(json_file_path)

    if data is None:
        return

    # 获取用户输入
    name_input = input("请输入文件名称（包括扩展名，例如 '实验一.png'）：")

    # 查找文件
    result = find_file_by_name(data, name_input)

    # 输出结果
    if result:
        print(f"文件名称: {result['name']}")
        print(f"文件路径: {result['path']}")
        print(f"文件大小: {result['size']}")
        print(f"创建日期: {result['createdDate']}")
    else:
        print("未找到该文件。")


if __name__ == '__main__':
    main()
