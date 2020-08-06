from . import parser 
from . import stringUtils

class AbstractHandler:

    # 需要特殊处理的字段，初步设想是根据event，one-one map
    def get_queue_name(self):    
        return 'risk.postpersist.venmo_cashout'

    def parseValidate(self,filter_expression):
        return parser.parse(filter_expression)
    pass


class DecayHandler(AbstractHandler):

    def parse(self,brd):
        do_data=self.parse(brd.filter_expression)
        key=stringUtils.randomStr(10)
        do_data.update({
            brd.key_expression: key
        })
        content = {
            # // 从jira获取
            "release_date": "2020-05-06",
            "comment": "GRSVT-3589",
            # brd里面的  "container_type": "BANK_ROUTING", 前面加EVE_
            "container_type": "EVE_"+brd['container_type'],
            # brd里面的  "value_type": "Decay",
            "variable_type": brd['value_type'],
            # decay类型的变量不设置expect值
            "expected_value": [],
            # brd里面的
            # "filter_expression": "VenmoAddFundingInstrument.fundingInstrumentType == 'BANK' && VenmoAddFundingInstrument.bankConfirmationMethod == 'INSTANT_CONFIRMATION'",
            "validate": brd['filter_expression'],
            "queue_name": self.get_queue_name(),
            # 随机数，如果是accountnumber的话，就是19位随机数，所有我觉得，都用19位随机数吧
            "container_key": key,
            "do": do_data,
            "do_override": {},
            "data_injection": [],
            "negative_case": {
                "negative_test": bool(),
                "negative_do_override": {
                    # 条件设置成validate的反
                    "VenmoAddFundingInstrument.BankConfirmationMethod": "todo"
                },
                "expected_value": []
            },
            "is_legacy": bool(),
            "is_aerospike": bool('true')
        }
        return content
    pass
