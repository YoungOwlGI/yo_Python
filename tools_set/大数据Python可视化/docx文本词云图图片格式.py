from collections import Counter
from jieba import cut
from wordcloud import WordCloud
from docx import Document

# 读取 .docx 文件中的文本
def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

# 指定 docx 文件路径
docx_path = 'my.docx'  # 替换为实际的文件路径
text = read_docx(docx_path)

# 统计词频并生成词云
words = cut(text)
filtered_words = [word for word in words if word.strip()]  # 过滤空值
freq = Counter(filtered_words)

# 确保词频字典是有效的
print(freq)  # 查看词频统计的内容

wordcloud = (WordCloud(font_path='千图小兔体.ttf',  # 字体文件路径
                       width=3840, height=2160,
                       background_color='pink',
                       font_step=3,
                       stopwords={})
             .generate_from_frequencies(freq))

wordcloud.to_image().show()
wordcloud.to_file('wordcloud.png')  # 保存图片
