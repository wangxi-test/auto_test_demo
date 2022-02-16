from selenium import webdriver


# driver=webdriver.Chrome()
# driver.get('http://www.baidu.com')
# el=driver.find_element('id','kw')
# value=el.get_attribute('class')
#
# js="document.getElementById('su').setAttribute('value','sad')"
# driver.execute_script(js)
# js="document.getElementById('search-input').removeAttribute('readonly')"
# driver.execute_script(js)

from time import sleep

from selenium import webdriver

# 启动浏览器:浏览器首字母要大写，还要添加()
driver = webdriver.Chrome()
# 访问url:一定要在url中添加http://这样的内容,如果不加会报错，必须加//
driver.get('http://www.baidu.com')
# 输入‘秋水好蠢’：通过find element函数查找元素，一定是查找有对应属性的元素
# driver.find_element_by_name('wd').send_keys('虚竹')
# # 点击‘百度一下’按钮实现搜索
# driver.find_element_by_id('su').click()
# 添加等待
sleep(3)



el = driver.find_element('xpath', '//*[@id="10"]/h3/a')
# js精准定位到指定元素，并显示
js = "arguments[0].scrollIntoView()"
# 调用js执行器
driver.execute_script(js, el)

el = driver.find_element('xpath', '//*[@id="kw"]')
# js修改元素属性
js = 'arguments[0].removeAttribute("name")'
driver.execute_script(js, el)

