import os

from keywords.key_word_demo import KeyDemo
from selenium import webdriver
import pytest

# pytestmark =pytest.mark.skip()

def test_01_search():
    kd = KeyDemo('Chrome')
    kd.driver.implicitly_wait(10)
    kd.open('http://www.baidu.com')
    kd.wait(3)
    print(kd.title())
    kd.input('id','kw','深岩银河')
    kd.click('id','su')
    wc=kd.loctor('xpath','//*[@id="1"]/div/div/h3/a/em').text
    # assert wc == '深岩1银河' ,'断言错误，是你麻痹'



# option = webdriver.ChromeOptions()
# option.add_argument('disable-inforbars')
# option.add_argument('headless')
# kd = webdriver.Chrome(chrome_options=option)
# kd.get('http://www.baidu.com')
# print(kd.title)

if __name__ == '__main__':
    pytest.main(['-s','--pdb','test_case.py::test_01_search','--alluredir','./result_json'])
    os.system('allure generate ./result/ -o ./report_allure/   --clean')
