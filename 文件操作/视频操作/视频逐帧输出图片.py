import cv2


def extract_frames_from_video(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()
    count = 0

    while success:
        frame_path = f'{output_folder}/frame_{count}.jpg'
        cv2.imwrite(frame_path, frame)
        print(f'Saved {frame_path}')
        count += 1
        success, frame = cap.read()

    cap.release()

if __name__ == '__main__':
    video_path = 'abc.mp4'
    output_folder = 'output_frames'

    extract_frames_from_video(video_path, output_folder)
