from time import sleep

from selenium import webdriver


class KeyDemo:
    '''
    自动化中，用于对象的基本操作，是常使用的操作行为
    输入
    点击
    查找元素
    关闭浏览器
    元素等待
    断言校验等
    '''
    def __init__(self,type_):
        if type_ == 'Chrome':
             self.driver=webdriver.Chrome()

        elif type_ == 'FireFox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Ie()

    # 打开页面
    def open(self,url):
        self.driver.get(url)

    # 定位元素
    def loctor(self,name,value):
        return self.driver.find_element(name,value)

    # 输入
    def input(self,name,value,text_):
        self.loctor(name,value).send_keys(text_)

    # 点击
    def click(self,name,value):
        self.loctor(name,value).click()

    # 退出
    def quit(self):
        self.driver.quit()

    # 强制等待
    def wait(self,time_):
        sleep(time_)

    def title(self):
        self.driver.title


if __name__ == '__main__':
    KeyDemo('Chrome').open('http://www.baidu.com')
