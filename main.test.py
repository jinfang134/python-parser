

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
            self.assertDictEqual(obj, item['data'])

    # def test_parse2(self):
    #     validate='''
    #     RDAData.source_event=='ACCTCRT'&&((RDAData.cntry_code=='C2'&&RDAData.rawHdrs_pp_geo_loc!='CN')||(RDAData.cntry_code!='C2'&&RDAData.cntry_code!=RDAData.rawHdrs_pp_geo_loc))
    #     '''
    #      obj = parser.parse(validate)
    #     print('result is: ', obj)
    #     self.maxDiff = None
    #     self.assertDictEqual(obj, {
    #         "PaymentDebitPostProcess.TransactionType": "@",
    #         "PaymentDebitPostProcess.SenderParentId": "0",
    #         "PaymentDebitPostProcess.FundingTransactionTypeV2": "H",
    #         "PaymentDebitPostProcess.FundingStatus": "P",
    #         "PaymentDebitPostProcess.VerticalCategoryId": "jewelry"
    #     })


unittest.main()
