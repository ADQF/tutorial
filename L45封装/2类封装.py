import requests
from lxml import etree

class Github(object):
    def __init__(self):
        # 属性 公共变量 配置项 全局需要访问
        self.login_url = 'http://github.com/login'
        self.do_login_url = 'http://github.com/session'
        self.profile_url = 'https://github.com/settings/profile'
        self.headers = {

        }
        self.s = requests.Session()

    def get_csrf_token(self):
        resp = self.s.get(self.login_url)
        html_content = resp.text
        pattern = '//input[@name="authenticity_token"]/@value'
        dom = etree.HTML(html_content)
        authenticity_token = dom.xpath(pattern)[0]
        return authenticity_token

    def do_login(self, authenticity_token):
        params = {
            'authenticity_token': authenticity_token,
        }
        resp = self.s.get()
        resp.status_code
        print("登陆成功")
        return True

    def request_profile(self):
        """
        请求个人设置页
        :return:
        """
        # 请求个人页
        return resp.text

    def get_user_email(self, html_content):
        return email

    def get_user_name(self, html_content):
        return user_name

if __name__ == '__main__':
    github = Github()
    # authenticity_token
