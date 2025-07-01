import cv2
import os
import glob


def create_video_from_frames(input_folder, output_video_path, fps=30):
    # 获取所有符合模式的图片文件并按数字排序
    frame_files = glob.glob(os.path.join(input_folder, 'frame_*.jpg'))
    try:
        # 按文件名中的数字排序
        frame_files.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[1]))
    except (IndexError, ValueError) as e:
        print(f"错误：图片命名格式不正确 - {e}")
        return

    if not frame_files:
        print("错误：未找到任何帧图片")
        return

    # 读取第一帧获取视频尺寸
    first_frame = cv2.imread(frame_files[0])
    if first_frame is None:
        print(f"错误：无法读取首帧 {frame_files[0]}")
        return

    height, width, _ = first_frame.shape

    # 初始化视频写入器（MP4格式）
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 编码器参数
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    if not out.isOpened():
        print("错误：无法创建视频文件，请检查参数")
        return

    # 逐帧写入视频
    for frame_path in frame_files:
        frame = cv2.imread(frame_path)
        if frame is None:
            print(f"警告：跳过无法读取的帧 {os.path.basename(frame_path)}")
            continue

        # 验证帧尺寸一致性
        h, w = frame.shape[0], frame.shape[1]
        if h != height or w != width:
            print(f"警告：帧尺寸不一致 ({w}x{h} vs {width}x{height})，已跳过")
            continue

        out.write(frame)
        print(f"已写入：{os.path.basename(frame_path)}")

    out.release()
    print(f"视频成功生成：{os.path.abspath(output_video_path)}")


if __name__ == '__main__':
    input_folder = 'output_frames'  # 帧图片所在目录
    output_video = '复原视频.mp4'  # 输出视频文件名

    # 处理中文路径问题（Windows可能需要额外配置）
    if not os.path.exists(input_folder):
        print(f"错误：输入目录不存在 {os.path.abspath(input_folder)}")
    else:
        create_video_from_frames(input_folder, output_video, fps=30)