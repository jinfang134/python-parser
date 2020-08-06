
class AbstractHandler:

    def parseValidate(self):
        pass
    pass


class DecayHandler(AbstractHandler):

    def parse(self,brd):
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
            # 需要特殊处理的字段，初步设想是根据event，one-one map
            "queue_name": "risk.postpersist.venmo_cashout",
            # 随机数，如果是accountnumber的话，就是19位随机数，所有我觉得，都用19位随机数吧
            "container_key": "E8SBQ30QH4",
            "do": {
                # 这个是key的值，字段对应的是      "key_expression": "VenmoAddFundingInstrument.bankRoutingNumber",
                "VenmoAddFundingInstrument.BankRoutingNumber": "E8SBQ30QH4",
                # 解析validate，首字母大写，    特殊字符有位运算 == != > <等等
                "VenmoAddFundingInstrument.FundingInstrumentType": "BANK",
                "VenmoAddFundingInstrument.BankConfirmationMethod": "INSTANT_CONFIRMATION"
            },
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
