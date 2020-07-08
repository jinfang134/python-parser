import re
#  PaymentDebitPostProcess.transactionType == '@' \
# && (PaymentDebitPostProcess.senderParentId == 0 || PaymentDebitPostProcess.senderParentId == null || PaymentDebitPostProcess.senderParentId == '') \
# && PaymentDebitPostProcess.fundingTransactionTypeV2== 'H' \
# && (PaymentDebitPostProcess.fundingStatus == 'P' || PaymentDebitPostProcess.fundingStatus == 'R') && PaymentDebitPostProcess.verticalCategoryId.indexOf('jewelry') >= 0


PATTERN_INDEXOF = r"(\w+)\.(\w+)\.indexOf\('(.*)'\)\s?>=\s?0"
PATTERN_EQUAL = r"(\w+)\.(\w+)\s?[=,>,<]=\s?([\w@#']+)"



def parse(express):
    result = {}
    eq_result = compile(PATTERN_EQUAL, express)
    result = mergeDic(result, eq_result)
    index_result = compile(PATTERN_INDEXOF, express)
    result = mergeDic(result, index_result)
    try:
        success=validate(express,result)
        if success:
            print('解析成功！！！')
    except (RuntimeError):
        print('部分解析失败')
    return result


# 合并两个dict，如果dica已经存在的属性，不进行覆盖
def mergeDic(dica, dicb):
    result = dica
    for item in dicb.keys():
        if item not in dica.keys():
            result[item] = dicb[item]
    return result


def compile(pattern, origin):
    result = {}
    equal_pattern = re.compile(pattern)
    list = equal_pattern.findall(origin)
    for item in list:
        key = item[0]+'.'+item[1]
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
            temp = temp.replace(key, result[key])
        else:
            temp = temp.replace(key, f"'{result[key]}'")
    print(temp)
    return eval(temp)



def upperFirst(str):
    return str[0:1].upper()+str[1:]



originStr = '''PaymentDebitPostProcess.transactionType == '@' \
&& (PaymentDebitPostProcess.senderParentId == 0 || PaymentDebitPostProcess.senderParentId == null || PaymentDebitPostProcess.senderParentId == '') \
&& PaymentDebitPostProcess.fundingTransactionTypeV2== 'H' \
&& (PaymentDebitPostProcess.fundingStatus == 'P' || PaymentDebitPostProcess.fundingStatus == 'R') \
&& PaymentDebitPostProcess.verticalCategoryId.indexOf('jewelry') >= 0'''
parse(originStr)
