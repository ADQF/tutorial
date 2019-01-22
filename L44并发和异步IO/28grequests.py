# grequests




import grequests
import requests
import time

urls = [
    'http://img5.imgtn.bdimg.com/it/u=2075339344,1744258849&fm=26&gp=0.jpg',
    'http://img0.imgtn.bdimg.com/it/u=4243952562,1567156492&fm=11&gp=0.jpg',
    'http://img0.imgtn.bdimg.com/it/u=14190622,896236262&fm=26&gp=0.jpg',
    'https://www.baidu.com',
    'https://www.douban.com',
    'https://www.github.com'
]

# start_time = time.time()
# for url in urls:
#     try:
#         resp = requests.get(url)
#         print(resp.status_code)
#         if resp.status_code == 200:
#             print(resp.text)
#     except Exception as e:
#         print(e)
# end_time = time.time()
# print(end_time - start_time)


# 异步请求
start_time = time.time()
rs = (grequests.get(url) for url in urls)
resp_list = grequests.map(rs)
for resp in resp_list:
    if resp is None:
        print(resp.url, '你妈叫你回家吃饭了')
    else:
        print(resp.status_code)
        print(resp.content)
end_time = time.time()
print(start_time - end_time)


