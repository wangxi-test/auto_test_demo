from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


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
        try:
            self.driver= self.browser(type_)
        except Exception as e:
            print(e)
            self.driver= webdriver.Chrome()

    # 打开浏览器
    def browser(self,type_):
        return getattr(webdriver,type_)()

    # 进入页面
    def open(self,**kwargs):
        self.driver.get(kwargs['text'])

    # 定位元素
    def loctor(self,**kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['value'])

    # 输入
    def input(self,**kwargs):
        self.loctor(**kwargs).send_keys(kwargs['text'])

    # 点击
    def click(self,**kwargs):
        self.loctor(**kwargs).click()

    # 退出
    def quit(self,**kwargs):
        self.driver.quit()

    # 强制等待
    def wait(self,**kwargs):
        sleep(kwargs['text'])

    # 获取页面标题
    def title(self):
        return self.driver.title

    # 截屏
    def save_screen(self,**kwargs):
        self.driver.save_screenshot(kwargs['text'])

    # 鼠标悬停
    def hover(self,**kwargs):
        # 自动化悬停操作过程中，鼠标不能动，否则会干扰悬停操作，最好使用无头模式
        action=ActionChains(self.driver)
        action.move_to_element(self.loctor(**kwargs)).perform()

    # 文本断言校验
    def assert_text(self,fact_text,**kwargs):
        return self.loctor(**kwargs).text ==fact_text,'断言失败，期望结果为{}，实际结果为{}'.format(fact_text,self.loctor(name,value).text)

    # 隐式等待
    def hidden_sleep(self,**kwargs):
        self.driver.implicitly_wait(kwargs['text'])

    # 显示等待
    def obvious_sleep(self,**kwargs,):
        WebDriverWait(self.driver,kwargs['text'],0.5).until(lambda el:self.driver.find_element(**kwargs),message='显示等待的元素，没有找到')


if __name__ == '__main__':
    pass

