```js
{
  "r_bre_model_result_valid_non_distinct_last20_atom19": {
    "release_date": "2020-08-11",
    "comment": "GRSVT-4139",
    "variable_type": "lastk",
    "container_key": "1534526750322550708",
    "container_type": "EVE_ACCOUNT_CACHE",
    "validate": "ConsolidatedFundingModelResult.atom19 != -999.0",
    "queue_name": "risk.postpersist.venmo_cashout",
    "expected_value": [
      //对应给roll_up字段的两次赋值（赋值可以直接定成100，200）
      "\"100\",\"200\""
    ],
    "do": {
      "ConsolidatedFundingModelResult.ReceiverAccountNumber": "1534526750322550708",
      //这个是个特殊情况，validate条件和roll_up条件都对应的是这个字段
      //      "filter_expression": "ConsolidatedFundingModelResult.atom19 != -999.0",
      //      "rollup_expression": "ConsolidatedFundingModelResult.atom19"
      "ConsolidatedFundingModelResult.Atom19": "100"
    },
    "do_override": {
      "ConsolidatedFundingModelResult.Atom19": "200"
    },
    "data_injection": [],
    "is_aerospike": true,
    "negative_case": {
      "negative_test": true,
      "expected_value": [
        "\"100\""
      ],
      "negative_do_override": {
        //filter条件里面是!=，取反之后是==，取反比较难处理吧……
        "ConsolidatedFundingModelResult.Atom19": "-999"
      }
    }
  },
}

```

brd data:
```json
{
  "status": "Implemented",
  "capacity": 20,
  "name": "r_bre_model_result_valid_non_distinct_last20_atom19",
  "distinct": false,
  "container_type": "ACCOUNT_CACHE",
  "updated_logic": [
    {
      "key_expression": "ConsolidatedFundingModelResult.receiverAccountNumber",
      "triggered_event": "ConsolidatedFundingModelResult",
      "filter_expression": "ConsolidatedFundingModelResult.atom19 != -999.0",
      "rollup_expression": "ConsolidatedFundingModelResult.atom19"
    }
  ],
  "created_info": {
    "date": 1594977920067,
    "reason": "from EVE Builder",
    "by": "yuejin"
  },
  "value_type": "LastK",
  "rollup_value_type": "Double",
  "type": "WRITING_EDGE",
  "description": "For every receiver_account_number from EdgeConsolidatedFundingModelResultWorkflow, consider score is not -999 population, calculate lastK lastk of atom19"
}
```