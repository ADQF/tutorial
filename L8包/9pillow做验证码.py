# pillow例子2 随机生成验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def random_char():
    return chr(random.randint(20000, 25000))

# 随机数字
def random_num():
    return random.random(0, 9)

# 随机字体颜色 稍深
def random_color():
    return (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))

# 随机背景颜色
def random_color2():
    return (random.randint(30, 120), random.randint(30, 120), random.randint(30, 120))
from PIL import Image, ImageFilter
im = Image.open('demo.jpg')
# 生成空白背景图层
image = Image.new('RGB', size=(240, 60), color=im.save('demo2.jpg', 'jpeg'))
# 生成绘制对象
draw = ImageDraw.Draw(image)
# 字体对象 ，字体 ，字号
import random
# 循环像素点并填充颜色

for x in range(0, 241):
    for i in range(0, 61):
        draw.point(xy=(x, i), fill=random_color2())
# 生成文字
for t in range(0, 4):
    draw.text((60*t+20, random.randint(0, 20)), random_char(), font=random.choice([ImageFont.truetype('msyh.ttf', random.randint(20, 40)), ImageFont.truetype('msyhbd.ttf', random.randint(20, 40))]), fill=random_color())
# 加模糊滤镜
image = image.filter(ImageFilter.DETAIL)

# 保存
image.save('demo4.jpg', 'jpeg')

