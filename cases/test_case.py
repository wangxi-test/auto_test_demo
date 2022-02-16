import os

from keywords.key_word_demo import KeyDemo
from selenium import webdriver
import pytest
from common.excel_wr import ParseExcel

# pytestmark =pytest.mark.skip()

def test_01_search():
    sheet=ParseExcel('../data/测试数据.xlsx').get_sheet_by_name('Sheet')
    for value in sheet.values:
        args = {}
        args['method'] = value[1]
        args['name'] = value[2]
        args['value'] =value[3]
        args['text']=value[4]
        # 判断是否为测试用例
        if type(value[0]) is int:
            # 判断是否实例化浏览器
            if value[1] == 'browser':
                driver=KeyDemo('Chrome')
            else:
                getattr(driver,value[1])(**args)


    # kd = KeyDemo('Chrome')
    # kd.driver.implicitly_wait(10)
    # kd.open('http://www.baidu.com')
    # kd.wait(3)
    # print(kd.title())
    # kd.input('id','kw','深岩银河')
    # kd.click('id','su')
    # kd.save_screen('./image/baidu.png')
    # wc=kd.loctor('xpath','//*[@id="1"]/div/div/h3/a/em').text
    # assert wc == '深岩1银河' ,'断言错误，是你麻痹'


if __name__ == '__main__':
    test_01_search()
    # pytest.main(['-s','--pdb','test_case.py::test_01_search','--alluredir','./result_json'])
    # os.system('allure generate ./result/ -o ./report_allure/   --clean')
