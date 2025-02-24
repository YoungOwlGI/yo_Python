from PIL import Image


def mirror_image(image_path, output_filename, mirror_type='horizontal'):
    """
    镜像图片函数。

    :param image_path: 输入图片的路径
    :param output_filename: 输出图片的文件名（包含扩展名）
    :param mirror_type: 镜像类型，可以是 'horizontal' 或 'vertical'
    """
    # 打开图片
    image = Image.open(image_path)

    # 根据选择的镜像类型进行翻转
    if mirror_type == 'horizontal':
        mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif mirror_type == 'vertical':
        mirrored_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Invalid mirror_type. Must be 'horizontal' or 'vertical'.")

        # 保存镜像后的图片，使用指定的输出文件名
    mirrored_image.save(output_filename)


# 使用函数来镜像图片，并指定输出文件名为 "00.png"
# （输入图片，输出图片，镜像类型）
mirror_image('22.png', '00.png', 'horizontal')