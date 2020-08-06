from src.factory import BrdHandlerFactory
from src.handler import AbstractHandler

import unittest


class NamesTestCase(unittest.TestCase):
    '''
    测试生成名字函数的类
    '''

    def test_factory(self):
        handler = BrdHandlerFactory.getBrdHandler('decay')
        self.assertIsInstance(handler, AbstractHandler)
        pass


unittest.main()
