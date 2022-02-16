from selenium import webdriver


# 配置chromeoption,一个配置类进行存放(都是固定写法)
class Option:
    def options_conf(self):
        # 创建opstion对象:用于配置浏览器的设置
        options = webdriver.ChromeOptions()
        # 去掉默认的自动化最上方横条提示
        options.add_experimental_option('excludeSwitches',['enable-automation'])

        # 去除日志信息
        # options.add_experimental_option('excludeSwitches',['enable-logging'])

        # 窗体最大化
        options.add_argument('start-maximized')

        # 加载本地缓存
        options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Temp\scoped_dir17824_313538496\Default')

        # 添加去掉保存账号密码的弹窗,防止干扰操作
        prefs={}
        prefs['credentials_enable_service']=False
        prefs['profile.password_manager_enabled']=False
        options.add_experimental_option("prefs",prefs)

        # 无界面模式运行
        # options.add_argument('--headless')

        # 无痕模式
        # options.add_argument('incognito')

        # 去掉指定等级的日志信息
        options.add_argument('log-level=3')    #  INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0

        return options

if __name__ == '__main__':
    options=Option().options_conf()
    driver = webdriver.Chrome(options=options)
