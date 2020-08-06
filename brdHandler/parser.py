import re
import stringUtils
from collectionUtils import mergeDic


PATTERN_INDEXOF = r"(\w+)\.(\w+)\.indexOf\('(.*)'\)\s?>=\s?0"
PATTERN_EQUAL = r"(\w+)\.(\w+)\s?[=,>,<]=\s?([\w@#']+)"


def parse(express, initData={}):
    """解析条件表达式，返回能够满足条件表达式的测试数据

    Args:
        express ([string]]): 要解析的条件表达式
        initData (dict, optional): [初始化数据，用于条件表达式中右侧的数据填充]. Defaults to {}.

    Returns:
        [type]: [生成的测试数据]
    """
    result = {}
    eq_result = compile(PATTERN_EQUAL, express)
    result = mergeDic(result, eq_result)
    index_result = compile(PATTERN_INDEXOF, express)
    result = mergeDic(result, index_result)
    success = validate(express, mergeDic(result, initData))
    if success:
        print('解析成功！！！')
    else:
        print('部分解析失败')
    print(result)
    return result


def compile(pattern, origin):
    result = {}
    equal_pattern = re.compile(pattern)
    list = equal_pattern.findall(origin)
    for item in list:
        key = item[0]+'.'+stringUtils.upperFirst(item[1])
        result[key] = str(item[2].replace('\'', ''))
    return result

# 将测试数据代入表达式，验证数据是否符合逻辑表达式的要求，
#　originExpress: 原始的逻辑表达式
#  result: 测试数据


def validate(originExpress, result):
    temp = originExpress
    temp = temp.replace('&&', ' and ')
    temp = temp.replace('||', ' or ')
    temp = temp.replace('indexOf', 'index')
    temp = temp.replace('null', 'None')
    for key in result.keys():
        if result[key].isdigit():
            temp = stringUtils.replaceIgnoreCase(temp, key, result[key])
        else:
            temp = stringUtils.replaceIgnoreCase(temp, key, f"'{result[key]}'")
    try:
        return eval(temp)
    except (NameError):
        print('解析失败，解析结果如下，请检查！')
        print(temp)
        return bool()


originStr = '''RDAData.source_event=='ACCTCRT'&&((RDAData.cntry_code=='C2'&&RDAData.rawHdrs_pp_geo_loc!='CN')||(RDAData.cntry_code!='C2'&&RDAData.cntry_code!=RDAData.rawHdrs_pp_geo_loc))'''
parse(originStr, {
    "RDAData.rawHdrs_pp_geo_loc": 'JA'
})
