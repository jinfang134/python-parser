```json
{
  "app_guid_rda_addcc_cnt_sw72":
  //sliding_window里面分四种
          //1.cnt_72:       没有roll_up字段       "expected_value": [",2,2,2"],  [",1,1,1"],
          //2.cnt_90：      没有roll_up字段       "expected_value": ["2,,2,2"],  ["1,,1,1"],
          //3.amt_72        有roll_up字段         "expected_value": [",100,100,100"],   字段对应brd里面的rollup_expression
          //4.amt_90        有roll_up字段         "expected_value": [",100,100,100"],   字段对应brd里面的rollup_expression
  {
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
      "negative_test": true
    },
    "is_legacy": false,
    "is_aerospike": true
  },
}
```

```json
{
  "name": "app_guid_rda_addcc_cnt_sw72",
  "type": "WRITING_EDGE",
  "status": "Implemented",
  "description": "For every rda_app_guid from EdgeRiskRDAConsolidatedDOWorkflow, consider addcc attempt events population, calculate slidingwindow count",
  "value_type": "SlidingWindow",
  "created_info": {
    "reason": "from EVE Builder",
    "by": "tinxia",
    "date": 1591082324721
  },
  "container_type": "",
  "updated_logic": [
    {
      "triggered_event": "Risk::RDAConsolidatedDO",
      "key_expression": "RDAData.rda_app_guid",
      "filter_expression": "RDAData.source_event=='DCSNRSLT_ADDCC'&&RDAData.accountNumber!='0'",
      "rollup_expression": "1"
    }
  ],
  "aggregation_type": "CNT",
  "bucket_specs": [
    {
      "size": "5m",
      "number": 12
    },
    {
      "size": "30m",
      "number": 48
    },
    {
      "size": "1h",
      "number": 72
    }
  ]
}
```