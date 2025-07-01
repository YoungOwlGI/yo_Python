import ffmpeg
import glob

# 匹配所有M4S文件的模式
m4s_files = glob.glob('11.m4s')
# 输出的MP4文件路径
output_mp4_file = 'output.mp4'

# 创建一个临时的文本文件来保存FFmpeg的输入文件列表
with open('input_files.txt', 'w') as f:
    for m4s_file in m4s_files:
        f.write('file \'%s\'\n' % m4s_file)

# 调用FFmpeg进行转换
ffmpeg.command(
    output=(output_mp4_file, '-f', 'concat', '-safe', '0', '-i', 'input_files.txt', '-c', 'copy'),
    input=''
).run(capture_stdout=True, capture_stderr=True)

# 删除临时文件
import os
os.remove('input_files.txt')