# wordcloud词云
# 作用：根据词汇和词频生成一张美观的词汇组成的图片，用于数据可视化。经常与jieba包\matplotlib一起使用。
# matplotlib : 绘制图表库   pip install matplotlib
# 官方仓库（注意github中搜索word_cloud而不是wordcloud）https://github.com/amueller/word_cloud
# 安装 pip install wordcloud

from wordcloud import WordCloud

# 用来生成词云的字符串用空格表示分词
string = """老师 加 考虑 商 老师 djfdfweiof 发刷卡的 老师 分拉考虑大 老师 里克的 附近 开水考虑是考虑到 金粉世家 快 老师 了 刷卡 的 积分 离开 家 水电费 """
string2 = """
Importance of relative word frequencies for font-size. With relative_scaling=0, only word-ranks are considered. With relative_scaling=1, a word that is twice as frequent will have twice the size. If you want to consider the word frequencies and not only their rank, relative_scaling around .5 often looks good
"""
# font = 'C:\\Windows\\Fonts\\msyh.ttc'
font = 'msyh.ttc'
wc = WordCloud(font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=1000,
               height=800,
               # max_font_size=300,
               min_font_size=50,
               ).generate(string)
wc.to_file('2词云.png')  # 保存图片







