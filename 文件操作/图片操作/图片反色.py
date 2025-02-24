from PIL import Image  
  
def invert_image(image_path, output_path):  
    # 打开图片  
    img = Image.open(image_path)  
  
    # 将图片转换为RGB模式  
    img = img.convert('RGB')  
  
    # 使用point函数对图片的每个像素进行操作  
    inverted_img = img.point(lambda p: 255-p)  
  
    # 保存反色后的图片  
    inverted_img.save(output_path)  
  
# 使用函数  
invert_image('微信图片_20240304215849.png', 'output.jpg')