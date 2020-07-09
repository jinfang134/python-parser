

import unittest
import parser
import json


class NamesTestCase(unittest.TestCase):
    '''
    测试生成名字函数的类
    '''

    def loadJson(self):
        with open('./data.json', 'r') as fo:
            data = json.load(fo)
            return data

    def test_parse(self):
        list = self.loadJson()
        for item in list:
            obj = parser.parse(item['validate'])
            print('result is: ', obj)
            self.maxDiff = None
            self.assertTrue(parser.validate(item['validate'],obj))

    def test_validate(self):
        str = '''PaymentDebitPostProcess.transactionType == '@' \
&& (PaymentDebitPostProcess.senderParentId == 0 || PaymentDebitPostProcess.senderParentId == null || PaymentDebitPostProcess.senderParentId == '') \
&& PaymentDebitPostProcess.fundingTransactionTypeV2== 'H' \
&& (PaymentDebitPostProcess.fundingStatus == 'P' || PaymentDebitPostProcess.fundingStatus == 'R') \
&& PaymentDebitPostProcess.verticalCategoryId.indexOf('jewelry') >= 0'''
        result = parser.validate(str, {
            "PaymentDebitPostProcess.transactionType": "@",
            "PaymentDebitPostProcess.senderParentId": "0",
            "PaymentDebitPostProcess.fundingTransactionTypeV2": "H",
            "PaymentDebitPostProcess.fundingStatus": "P",
            "PaymentDebitPostProcess.verticalCategoryId": "jewelry"
        })
        self.assertTrue(result)

    def test_replace(self):
        result=parser.replaceIgnoreCase('test Hello','hello','world')
        self.assertEqual(result,'test world')

unittest.main()
