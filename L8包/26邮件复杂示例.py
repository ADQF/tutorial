import yagmail
import os

sender = '3342899060@qq.com'
password = 'imzlhndcfngzcjja'
target = '1596172625@qq.com'


html = """
<html lang="zh">
    <head>
        <meta charset="utf-8">
        <title>示例2</title>
    </head>
    <body>
        <h1>测试</h1>
        <p>lalalalalala</p>
        <img src="https://www.baidu.com/img/bd_logo1.png"/>
    </body>
</html>
"""
attachment_path = os.path.join(os.path.dirname(__file__), 'bose.png')
print(attachment_path)

contents = ['测试yagmail示例2', html, attachment_path]

yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', port=465, smtp_ssl=True)

yag.send(to=target, subject='测试yagmail示例2', contents=contents)
print('已发送')

