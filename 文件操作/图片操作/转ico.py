from PIL import Image


def convert_to_ico(input_image_path, output_ico_path, size=(256, 256)):
    """
    将PNG或JPG图像转换为ICO格式。

    :param input_image_path: 输入图像（PNG或JPG）的路径。
    :param output_ico_path: 输出ICO文件将被保存的路径。
    :param size: 结果图标的尺寸。一个包含（宽度，高度）的元组。
    """
    # 打开图像文件  
    img = Image.open(input_image_path)

    # 如果有需要，可以调整图像大小  
    img = img.resize(size)

    # 保存为ICO格式  
    img.save(output_ico_path, format='ICO')


# 使用函数进行转换  
input_png_path = 'favicon.png'  # 替换为你的PNG图片路径
output_ico_path = 'facicon.ico'  # 输出ICO文件的路径
convert_to_ico(input_png_path, output_ico_path)
