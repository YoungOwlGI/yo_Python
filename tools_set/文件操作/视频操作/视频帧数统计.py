import cv2
import os


def count_frames_in_video(video_path):
    # 尝试打开视频文件 
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"错误：无法打开视频文件 {video_path}")
        return -1

    count = 0
    while True:
        success, frame = cap.read()
        if not success:
            break  # 视频读取结束或出错时退出 
        count += 1

    cap.release()
    return count


if __name__ == '__main__':
    # 处理中文路径问题（Windows可能需要）
    video_path = '《崩坏：星穹铁道》「2025星铁LIVE」演唱会官方录播完整版.mp4'

    # 测试路径是否存在 
    if not os.path.exists(video_path):
        print(f"错误：视频文件不存在 {os.path.abspath(video_path)}")
    else:
        frame_count = count_frames_in_video(video_path)
        if frame_count >= 0:
            print(f"视频 '{video_path}' 共有 {frame_count} 帧")