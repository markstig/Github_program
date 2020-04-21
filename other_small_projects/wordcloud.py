from wordcloud import WordCloud
import jieba
import PIL.Image as Image
import numpy
import pyperclip

# 不想显示的文字，过滤文字
stopword = {"傻逼", "辣鸡"}
 
#将文本中的这个词认为一个词
jieba.add_word="is"
 
 
# 定义一个中文的分词函数
def chinese_word(text):
    #将文本分词
    wordlist_jieba = jieba.cut(text)
    #分出来的词用空格连接起来
    wl_space_split = " ".join(wordlist_jieba)
    return wl_space_split

text = pyperclip.paste()

cn_text = chinese_word(text)  # 调用中文分词函数
mask_pic = numpy.array(Image.open("/users/markli/downloads/download.jpeg"))  # 加载图片做背景
# 生成词云的核心代码，指定背景颜色、字体、最多多少个单词、过滤噪音文字、添加背景图片
# 必须加字体，否则中文不显示
# 如果没有图片做背景，可以在WordCoud()中加入windth 和height 来控制图片大小
wordcloud = WordCloud(background_color="white",font_path='/System/Library/fonts/PingFang.ttc', mask=mask_pic, max_words=20000,stopwords=stopword).generate(text)
image = wordcloud.to_image()  # 出图
image.show()  # 打开图片
wordcloud.to_file("/users/markli/downloads/generated_pic.jpg")  # 保存图片到