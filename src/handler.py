from . import parser
from . import stringUtils


class AbstractHandler:

    # 需要特殊处理的字段，初步设想是根据event，one-one map
    def get_queue_name(self):
        return 'risk.postpersist.venmo_cashout'

    def parseValidate(self, filter_expression):
        return parser.parse(filter_expression)

    def handle(self, brd):
        pass

    def get_key(self):
        pass


class DecayHandler(AbstractHandler):

    def get_key(self, brd):
        """  "bank_routing_vm_addfi_instnt_bank_cnt_5":
  //decay类型的variable的name有一些特殊，由brd中的三部分合成：
          //  "name": "bank_routing_vm_addfi_instnt_bank",
          //  "aggregation_type": ["CNT"],
          // "factors": [5,10,20,40,80 ],
        Args:
            brd ([type]): [description]
        """
        return brd['name']+'_'+brd['aggregation_type']+'_'+brd['factors'][0]

    def handle(self, brd):
        do_data = self.parseValidate(brd.filter_expression)
        key = stringUtils.randomStr(10)
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
        return {self.get_key(brd): content}


class LastkHandler(AbstractHandler):
    def get_key(self, brd):
        return brd.name

    def handle(self, brd):
        container_key = stringUtils.randomNumber(19)
        content = {
            "release_date": "2020-08-11",
            "comment": "GRSVT-4139",
            "variable_type": "lastk",
            "container_key": container_key,
            "container_type": "EVE_"+brd['container_type'],
            "validate": brd['filter_expression'],
            "queue_name": "risk.postpersist.venmo_cashout",
            "expected_value": [
                # 对应给roll_up字段的两次赋值（赋值可以直接定成100，200）
                "\"100\",\"200\""
            ],
            "do": {
                "ConsolidatedFundingModelResult.ReceiverAccountNumber": container_key,
                # 这个是个特殊情况，validate条件和roll_up条件都对应的是这个字段
                # "filter_expression": "ConsolidatedFundingModelResult.atom19 != -999.0",
                # "rollup_expression": "ConsolidatedFundingModelResult.atom19"
                "ConsolidatedFundingModelResult.Atom19": "100"
            },
            "do_override": {
                "ConsolidatedFundingModelResult.Atom19": "200"
            },
            "data_injection": [],
            "is_aerospike": bool(1),
            "negative_case": {
                "negative_test": bool(1),
                "expected_value": [
                    "\"100\""
                ],
                "negative_do_override": {
                    # filter条件里面是 !=，取反之后是 ==，取反比较难处理吧……
                    "ConsolidatedFundingModelResult.Atom19": "-999"
                }
            }
        }
        return {self.get_key(brd): content}


class SlidingHandler(AbstractHandler):
    def get_key(self, brd):
        return brd['name']

    def handle(self, brd):
        content = {
            "release_date": "2020-06-16",
            "comment": "GRSVT-3911",
            "container_type": "EVE_DEVICE_APP",
            "variable_type": "sliding_window",
            "expected_value": [
                ",2,2,2"
            ],
            "validate": "RDAData.source_event=='DCSNRSLT_ADDCC'&&RDAData.accountNumber!='0'",
            "queue_name": "risk.postpersist.venmo_cashout",
            "container_key": "UB93MSOJ1D",
            "do": {
                "RDAData.Rda_app_guid": "UB93MSOJ1D",
                "RDAData.Source_event": "DCSNRSLT_ADDCC",
                "RDAData.AccountNumber": "1"
            },
            "do_override": {},
            "data_injection": [],
            "negative_case": {
                "expected_value": [
                    ",1,1,1"
                ],
                "negative_do_override": {
                    "RDAData.Source_event": "TODO"
                },
                "negative_test": bool('true')
            },
            "is_legacy": bool(),
            "is_aerospike": bool('true')
        }
        return {self.get_key(brd): content}
