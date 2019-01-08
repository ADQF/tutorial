ids = [1, 2, 3, 5, 5, 1, 3]
news_ids = []
for id in ids:                # 循环第一个列表
    if id not in news_ids:    # 第一个列表不在第二个列表中，就输出，在的话删除
        news_ids.append(id)
print(news_ids)


ids = [1, 2, 3, 5, 5, 1, 3]
news_ids = []
v=()
for id in ids:
    if id > ids:
        v = id
