#错的
import pytesseract
from pytesseract import Output
import cv2


def extract_text_from_frame(frame):
    # 将帧转换为灰度图像，因为Tesseract在灰度图像上工作得更好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用pytesseract从灰度图像中提取文本
    text = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')
    return text


def process_text(text):
    # 在这里处理提取的文本，比如打印出来或进行其他操作
    print(text)


video = cv2.VideoCapture('11111.mp4')
while True:
    ret, frame = video.read()
    if not ret:
        break
    else:
        text = extract_text_from_frame(frame)
        process_text(text)

    # 释放视频对象
video.release()
# 关闭所有OpenCV窗口
cv2.destroyAllWindows()