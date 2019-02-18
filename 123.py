import jieba
import wordcloud
from scipy.misc import imread
print("请输入文件名(列：g.png)",end='')
a=input("")
print("请输入形状文件名（列：g.png）",end='')
b=input('')
mask=imread(b)
f = open("临时.txt", "r")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud( font_path = "msyh.ttc",\
width = 1000, height = 700, background_color ="white",mode="RGBA",\
stopwords={"一个","形成","完成"},mask=mask,\
min_font_size=6)
w.generate(txt)
w.to_file(a)
