from src.factory import BrdHandlerFactory
from src.handler import AbstractHandler

import unittest


class NamesTestCase(unittest.TestCase):
    '''
    测试生成名字函数的类
    '''

    def test_factory(self):
        brd_list = []
        for brd in brd_list:
            handler = BrdHandlerFactory.getBrdHandler(brd['type'])
            obj = handler.handle(brd)
        self.assertIsInstance(handler, AbstractHandler)
        pass


unittest.main()
