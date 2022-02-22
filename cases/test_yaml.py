import unittest

from ddt import ddt, file_data
from keywords.key_word_yaml import BasePage
from selenium import webdriver

@ddt
class Demo(unittest.TestCase):
    def setUp(self) -> None:
        self.wk = BasePage(webdriver.Chrome())

    def tearDown(self) -> None:
        pass
    @file_data('../data/search.yaml')
    def test_01(self,**kwargs):
        self.wk.open(kwargs['url'])
        self.wk.wait(kwargs['time'])
        self.wk.input(**kwargs['input'])
        self.wk.click(**kwargs['click'])
        self.wk.save_screen(kwargs['path'])


if __name__ == '__main__':
    unittest.main()