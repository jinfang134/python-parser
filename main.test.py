

import unittest
import parser


class NamesTestCase(unittest.TestCase):
    '''
    测试生成名字函数的类
    '''

    def test_parse(self):
        validate = '''
        PaymentDebitPostProcess.transactionType == '@' \
        && (PaymentDebitPostProcess.senderParentId == 0 || PaymentDebitPostProcess.senderParentId == null || PaymentDebitPostProcess.senderParentId == '') \
        && PaymentDebitPostProcess.fundingTransactionTypeV2== 'H' \
        && (PaymentDebitPostProcess.fundingStatus == 'P' || PaymentDebitPostProcess.fundingStatus == 'R') && PaymentDebitPostProcess.verticalCategoryId.indexOf('jewelry') >= 0
        '''
        obj = parser.parse(validate)
        print('result is: ', obj)
        self.maxDiff = None
        self.assertDictEqual(obj, {
            "PaymentDebitPostProcess.TransactionType": "@",
            "PaymentDebitPostProcess.SenderParentId": "0",
            "PaymentDebitPostProcess.FundingTransactionTypeV2": "H",
            "PaymentDebitPostProcess.FundingStatus": "P",
            "PaymentDebitPostProcess.VerticalCategoryId": "jewelry"
        })


unittest.main()
