import yagmail
import os

sender = '3342899060@qq.com'
password = 'imzlhndcfngzcjja'
target = '1770323960@qq.com'

yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', port=465, smtp_ssl=True)
contents = '测试test'
yag.send(to=target, subject='测试yagmail发邮件', contents=contents)
print('已发送')

