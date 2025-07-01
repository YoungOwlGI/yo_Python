import cv2
import os


def extract_frames_from_video(video_path, output_folder):
    # 确保输出目录存在
    os.makedirs(output_folder, exist_ok=True)

    # 尝试打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"错误：无法打开视频文件 {video_path}")
        return

    count = 0
    while True:
        success, frame = cap.read()
        if not success:
            break  # 视频读取结束或出错时退出

        frame_path = os.path.join(output_folder, f'frame_{count}.jpg')
        # 验证帧是否有效
        if frame is None:
            print(f"警告：第 {count} 帧为空，跳过保存")
            continue

        # 保存帧并验证
        if cv2.imwrite(frame_path, frame):
            print(f'已保存：{frame_path}')
        else:
            print(f'保存失败：{frame_path}')
        count += 1

    cap.release()


if __name__ == '__main__':
    # 处理中文路径问题（Windows可能需要）
    video_path = '20250624_213550.mp4'
    output_folder = 'output_frames'

    # 测试路径是否存在
    if not os.path.exists(video_path):
        print(f"错误：视频文件不存在 {os.path.abspath(video_path)}")
    else:
        extract_frames_from_video(video_path, output_folder)