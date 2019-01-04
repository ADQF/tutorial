# jieba分词
# 作用：把一句话 按照词汇分隔，为后面的词频统计和图片展示打基础。

import jieba
import pymysql

results = jieba.cut('把一句话 按照词汇分隔，为后面的词频统计和图片展示打基础。', cut_all=False)


word_list = []
for r in results:
    print(r)
    word_list.append(r)
print(word_list)

for r in results:
    print('生成器只能取一次', r)

print(results)


"""
生成器generator， 参考L4/L5小节。
跟列表相比：
1. 都是可迭代的，被for循环。range(0,10)返回的就是生成器。
2. generator优点用一个去一个，占内存低。
3. 循环后才能看到数据不太直观
"""
