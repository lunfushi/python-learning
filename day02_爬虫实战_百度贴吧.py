#百度贴吧搜索“奥迪”
#https://tieba.baidu.com/f/search/res?qw=%E5%A5%A5%E8%BF%AA&ie=utf-8
#百度贴吧搜索“宝马”
#https://tieba.baidu.com/f/search/res?qw=%E5%AE%9D%E9%A9%AC&ie=utf-8
#百度贴吧搜索“奔驰”
#https://tieba.baidu.com/f/search/res?qw=%E5%A5%94%E9%A9%B0&ie=utf-8

import requests
from urllib.parse import quote
# str1="电影"
# print(quote(str1))
class Spider(object):
    def __init__(self):
        """
        爬虫原理的第一步：准备数据
        """
        self.start_url='https://tieba.baidu.com/f/search/res?qw={}&ie=utf-8'  #此处为百度贴吧改新版后的url
        self.user_input=input("请输入你想采集的贴吧主题<示例：宝马>")
        self.user_input="宝马"
        self.headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                   "(KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"}
    def parse_start_url(self):
        """
        爬虫实战的第二步：发送请求，获取响应
        :return:
        """
        #for循环模拟翻页
        # for page in range(5): #旧版百度贴吧模式
        user_inp=quote(self.user_input)
        response=requests.get(self.start_url.format(user_inp),headers=self.headers).content.decode()
    def parse_response_data(self,response):
        """
        爬虫原理第三步：数据响应，数据提取
        :param response:
        :return:
        """
        #获取状态码
        code=response.status_code
        if code==200:
            #执行解析
            data=response.content.decode()
            self.parse_save_data(data)
    def parse_save_data(self,data):
        """
        爬虫原理第四步：保存数据
        :param data:
        :return:
        """
        with open(self.user_input + '' + '.html','w',encoding='utf-8') as f:
            f.write(data)
        print(f"贴吧：{self.user_input}---数据采集完成！")
if __name__ == "__main__":
    s=Spider()
    s.parse_start_url()

